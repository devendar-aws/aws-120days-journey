const API_URL = 'https://31l6g64o92.execute-api.ap-south-1.amazonaws.com/dev/todo'; // Replace with your actual URL

async function fetchTasks() {
    try {
        const response = await fetch(API_URL, {
            method: 'GET'
        });

        const result = await response.json();
        console.log("Raw fetch response:", result);

        let tasks = [];

        if (typeof result === 'object' && result.body) {
            try {
                tasks = JSON.parse(result.body); // Lambda proxy returns body as string
            } catch (e) {
                console.error("JSON.parse error on result.body:", e);
                return;
            }
        } else if (Array.isArray(result)) {
            tasks = result; // in case direct array is returned
        } else {
            console.error("Unexpected format in response:", result);
            return;
        }

        const taskList = document.getElementById('task-list');
        taskList.innerHTML = '';

        tasks.forEach(task => {
            const li = document.createElement('li');

            const infoDiv = document.createElement('div');
            infoDiv.className = 'task-info';
            infoDiv.textContent = `${task.taskId}: ${task.description} (${task.status})`;

            const actionsDiv = document.createElement('div');
            actionsDiv.className = 'task-actions';

            const editButton = document.createElement('button');
            editButton.textContent = 'Edit';
            editButton.onclick = () => editTask(task.taskId, task.description, task.status);

            const deleteButton = document.createElement('button');
            deleteButton.textContent = 'Delete';
            deleteButton.onclick = () => deleteTask(task.taskId);

            actionsDiv.appendChild(editButton);
            actionsDiv.appendChild(deleteButton);

            li.appendChild(infoDiv);
            li.appendChild(actionsDiv);

            taskList.appendChild(li);
        });
    } catch (error) {
        console.error("fetchTasks failed:", error);
    }
}

async function addTask() {
    const taskId = document.getElementById('taskId').value;
    const description = document.getElementById('description').value;
    const status = document.getElementById('status').value || 'Pending';

    const payload = { taskId, description, status };

    try {
        const response = await fetch(API_URL, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        });

        const result = await response.json();
        console.log("Add response:", result);

        fetchTasks();
    } catch (error) {
        console.error("addTask failed:", error);
    }
}

async function updateTask() {
    const taskId = document.getElementById('taskId').value;
    const description = document.getElementById('description').value;
    const status = document.getElementById('status').value;

    const payload = { taskId, description, status };

    try {
        const response = await fetch(API_URL, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        });

        const result = await response.json();
        console.log("Update response:", result);

        fetchTasks();
    } catch (error) {
        console.error("updateTask failed:", error);
    }
}

async function deleteTask(taskId) {
    const payload = { taskId };

    try {
        const response = await fetch(API_URL, {
            method: 'DELETE',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        });

        const result = await response.json();
        console.log("Delete response:", result);

        fetchTasks();
    } catch (error) {
        console.error("deleteTask failed:", error);
    }
}

function editTask(taskId, description, status) {
    document.getElementById('taskId').value = taskId;
    document.getElementById('description').value = description;
    document.getElementById('status').value = status;
}

// Initial load
fetchTasks();
