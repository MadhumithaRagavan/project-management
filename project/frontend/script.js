const API = "http://127.0.0.1:5000";

function addTask() {
    fetch(`${API}/add-task`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            subject: document.getElementById("subject").value,
            description: document.getElementById("description").value,
            hours: document.getElementById("hours").value
        })
    }).then(res => res.json())
      .then(data => {
          alert(data.message);
          loadTasks();
      });
}

function loadTasks() {
    fetch(`${API}/tasks`)
    .then(res => res.json())
    .then(data => {
        let list = document.getElementById("taskList");
        list.innerHTML = "";
        data.forEach(task => {
            list.innerHTML += `<li>${task.subject} - ${task.description} (${task.hours} hrs)</li>`;
        });
    });
}

function addMarks() {
    fetch(`${API}/add-marks`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            subject: document.getElementById("markSubject").value,
            marks: document.getElementById("marks").value
        })
    }).then(res => res.json())
      .then(data => {
          alert(data.message);
          loadPerformance();
      });
}

function loadPerformance() {
    fetch(`${API}/performance`)
    .then(res => res.json())
    .then(data => {
        let list = document.getElementById("performanceList");
        list.innerHTML = "";
        data.forEach(p => {
            list.innerHTML += `<li>${p.subject} - ${p.marks} Marks</li>`;
        });
    });
}

window.onload = function() {
    loadTasks();
    loadPerformance();
};