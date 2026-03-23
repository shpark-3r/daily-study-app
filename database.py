import sqlite3
import os
from datetime import date

DB_PATH = os.environ.get("DB_PATH", "study.db")


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS daily_tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            subject TEXT NOT NULL,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            checked INTEGER DEFAULT 0,
            sort_order INTEGER DEFAULT 0
        );
        CREATE INDEX IF NOT EXISTS idx_date ON daily_tasks(date);

        CREATE TABLE IF NOT EXISTS custom_tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            title TEXT NOT NULL,
            checked INTEGER DEFAULT 0
        );
        CREATE INDEX IF NOT EXISTS idx_custom_date ON custom_tasks(date);
    """)
    conn.commit()
    conn.close()
