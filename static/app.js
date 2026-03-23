let currentDate = new Date();

function formatDate(d) {
    return d.toISOString().split('T')[0];
}

function formatDisplay(d) {
    const days = ['일', '월', '화', '수', '목', '금', '토'];
    const m = d.getMonth() + 1;
    const day = d.getDate();
    const dow = days[d.getDay()];
    return `${m}월 ${day}일 (${dow})`;
}

function changeDate(delta) {
    currentDate.setDate(currentDate.getDate() + delta);
    loadTasks();
}

function goToday() {
    currentDate = new Date();
    loadTasks();
}

async function loadTasks() {
    const dateStr = formatDate(currentDate);
    document.getElementById('currentDate').textContent = formatDisplay(currentDate);

    try {
        const res = await fetch(`/api/tasks/${dateStr}`);
        const data = await res.json();
        renderDailyTasks(data.daily_tasks);
        renderCustomTasks(data.custom_tasks);
        updateProgress(data.daily_tasks, data.custom_tasks);
    } catch (e) {
        document.getElementById('tasksContainer').innerHTML =
            '<div class="loading">로드 실패. 새로고침 해주세요.</div>';
    }

    loadStats();
}

function renderDailyTasks(tasks) {
    const container = document.getElementById('tasksContainer');
    if (!tasks.length) {
        container.innerHTML = '<div class="loading">오늘의 학습 콘텐츠가 없습니다.</div>';
        return;
    }

    let html = '';
    let currentSubject = '';

    for (const task of tasks) {
        if (task.subject !== currentSubject) {
            currentSubject = task.subject;
            html += `<div class="subject-section"><div class="subject-label">${task.subject}</div>`;
        }

        const checkedClass = task.checked ? ' checked' : '';
        html += `
            <div class="task-card${checkedClass}" id="task-${task.id}">
                <div class="task-top" onclick="toggleDaily(${task.id}, ${!task.checked})">
                    <div class="checkbox"></div>
                    <div class="task-title">${task.title}</div>
                    <button class="expand-btn" onclick="event.stopPropagation(); toggleExpand(${task.id})">▼</button>
                </div>
                <div class="task-content">${task.content}</div>
            </div>
        `;
    }
    // Close last subject section
    html += '</div>';

    container.innerHTML = html;
}

function renderCustomTasks(tasks) {
    const container = document.getElementById('customContainer');
    if (!tasks.length) {
        container.innerHTML = '';
        return;
    }

    let html = '';
    for (const task of tasks) {
        const checkedClass = task.checked ? ' checked' : '';
        html += `
            <div class="custom-task${checkedClass}" id="custom-${task.id}">
                <div class="checkbox" onclick="toggleCustom(${task.id}, ${!task.checked})"></div>
                <div class="custom-task-title" onclick="toggleCustom(${task.id}, ${!task.checked})">${task.title}</div>
                <button class="delete-btn" onclick="deleteCustom(${task.id})">✕</button>
            </div>
        `;
    }
    container.innerHTML = html;
}

function updateProgress(daily, custom) {
    const all = [...daily, ...custom];
    const total = all.length;
    const done = all.filter(t => t.checked).length;
    const pct = total > 0 ? Math.round((done / total) * 100) : 0;

    document.getElementById('progressBar').style.width = pct + '%';
    document.getElementById('progressLabel').textContent = `${done} / ${total} 완료`;
    document.getElementById('progressPct').textContent = pct + '%';
}

async function toggleDaily(id, checked) {
    await fetch(`/api/tasks/daily/${id}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ checked }),
    });
    loadTasks();
}

async function toggleCustom(id, checked) {
    await fetch(`/api/tasks/custom/${id}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ checked }),
    });
    loadTasks();
}

async function addCustomTask() {
    const input = document.getElementById('customInput');
    const title = input.value.trim();
    if (!title) return;

    await fetch('/api/tasks/custom', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ date: formatDate(currentDate), title }),
    });
    input.value = '';
    loadTasks();
}

async function deleteCustom(id) {
    await fetch(`/api/tasks/custom/${id}`, { method: 'DELETE' });
    loadTasks();
}

function toggleExpand(id) {
    const card = document.getElementById(`task-${id}`);
    card.classList.toggle('expanded');
}

async function loadStats() {
    try {
        const res = await fetch('/api/stats?days=7');
        const data = await res.json();
        renderStats(data);
    } catch (e) { /* ignore */ }
}

function renderStats(stats) {
    const grid = document.getElementById('statsGrid');
    if (!stats.length) {
        grid.innerHTML = '<div style="grid-column:1/-1;text-align:center;color:var(--text2);font-size:0.8rem;">아직 데이터가 없습니다</div>';
        return;
    }

    let html = '';
    for (const s of stats.reverse()) {
        const pct = s.total > 0 ? Math.round((s.completed / s.total) * 100) : 0;
        const dateObj = new Date(s.date + 'T00:00:00');
        const label = `${dateObj.getMonth() + 1}/${dateObj.getDate()}`;
        let cls = 'low';
        if (pct >= 80) cls = 'high';
        else if (pct >= 40) cls = 'mid';

        html += `
            <div class="stat-day">
                <div class="stat-date">${label}</div>
                <div class="stat-pct ${cls}">${pct}%</div>
            </div>
        `;
    }
    grid.innerHTML = html;
}

// Init
loadTasks();
