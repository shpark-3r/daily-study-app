from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from datetime import date, datetime
import os

from database import get_db, init_db
from study_generator import generate_daily_tasks

app = FastAPI(title="Daily Study Checklist")


@app.on_event("startup")
def startup():
    init_db()


# --- API Models ---

class ToggleRequest(BaseModel):
    checked: bool


class CustomTaskCreate(BaseModel):
    date: str
    title: str


# --- API Routes ---

@app.get("/api/tasks/{date_str}")
def get_tasks(date_str: str):
    """Get all tasks for a given date. Auto-generates if not exists."""
    try:
        d = date.fromisoformat(date_str)
    except ValueError:
        raise HTTPException(400, "Invalid date format. Use YYYY-MM-DD")

    conn = get_db()

    # Check if daily tasks exist for this date
    existing = conn.execute(
        "SELECT COUNT(*) as cnt FROM daily_tasks WHERE date = ?", (date_str,)
    ).fetchone()

    if existing["cnt"] == 0:
        # Generate daily tasks
        tasks = generate_daily_tasks(d)
        for t in tasks:
            conn.execute(
                "INSERT INTO daily_tasks (date, subject, title, content, sort_order) VALUES (?, ?, ?, ?, ?)",
                (t["date"], t["subject"], t["title"], t["content"], t["sort_order"]),
            )
        conn.commit()

    # Fetch daily tasks
    daily = conn.execute(
        "SELECT id, date, subject, title, content, checked, sort_order FROM daily_tasks WHERE date = ? ORDER BY sort_order",
        (date_str,),
    ).fetchall()

    # Fetch custom tasks
    custom = conn.execute(
        "SELECT id, date, title, checked FROM custom_tasks WHERE date = ? ORDER BY id",
        (date_str,),
    ).fetchall()

    conn.close()

    return {
        "date": date_str,
        "daily_tasks": [dict(row) for row in daily],
        "custom_tasks": [dict(row) for row in custom],
    }


@app.put("/api/tasks/daily/{task_id}")
def toggle_daily_task(task_id: int, req: ToggleRequest):
    conn = get_db()
    conn.execute("UPDATE daily_tasks SET checked = ? WHERE id = ?", (int(req.checked), task_id))
    conn.commit()
    conn.close()
    return {"ok": True}


@app.put("/api/tasks/custom/{task_id}")
def toggle_custom_task(task_id: int, req: ToggleRequest):
    conn = get_db()
    conn.execute("UPDATE custom_tasks SET checked = ? WHERE id = ?", (int(req.checked), task_id))
    conn.commit()
    conn.close()
    return {"ok": True}


@app.post("/api/tasks/custom")
def add_custom_task(task: CustomTaskCreate):
    conn = get_db()
    cursor = conn.execute(
        "INSERT INTO custom_tasks (date, title) VALUES (?, ?)",
        (task.date, task.title),
    )
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()
    return {"id": new_id, "date": task.date, "title": task.title, "checked": 0}


@app.delete("/api/tasks/custom/{task_id}")
def delete_custom_task(task_id: int):
    conn = get_db()
    conn.execute("DELETE FROM custom_tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
    return {"ok": True}


@app.get("/api/stats")
def get_stats(days: int = 7):
    """Get completion stats for the last N days."""
    conn = get_db()
    rows = conn.execute("""
        SELECT date,
               COUNT(*) as total,
               SUM(checked) as completed
        FROM (
            SELECT date, checked FROM daily_tasks
            UNION ALL
            SELECT date, checked FROM custom_tasks
        )
        GROUP BY date
        ORDER BY date DESC
        LIMIT ?
    """, (days,)).fetchall()
    conn.close()
    return [dict(r) for r in rows]


# --- Static files ---
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def index():
    return FileResponse("static/index.html")


if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
