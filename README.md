**Full-Stack Study Planner and Academic Performance Tracker**
**Project Overview:**

The Full-Stack Study Planner and Academic Performance Tracker is a web-based application designed to help students efficiently manage study tasks and monitor academic performance. The system allows users to add subject-wise study tasks, allocate study hours, and record academic marks in a structured environment. The application is developed using Flask for the backend, SQLite for database management, and HTML, CSS, and JavaScript for the frontend interface. It demonstrates complete frontend-backend integration using RESTful APIs.

**Features:**

The system enables users to create study tasks with subject name, description, and allocated hours. It allows tracking of academic marks for performance monitoring. The application dynamically updates data using asynchronous API calls and maintains persistent records using a relational database. The interface follows a clean dashboard layout to ensure usability and clarity.

**Technology Stack:**

The backend is implemented using Python with the Flask framework. Flask-SQLAlchemy is used for Object Relational Mapping (ORM) and database operations. SQLite serves as the lightweight database. The frontend is built using HTML5 for structure, CSS3 for styling, and JavaScript using the Fetch API for communication with backend services.

**Project Structure:**
study-planner/
│
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── database.db
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
└── README.md
**Backend Implementation:**

The backend handles API requests and database operations using Flask and SQLAlchemy.

**Database Models:**
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(100))
    description = db.Column(db.String(200))
    hours = db.Column(db.Integer)
    status = db.Column(db.String(50))

class Performance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(100))
    marks = db.Column(db.Integer)
**Add Task API:**
@app.route('/add-task', methods=['POST'])
def add_task():
    data = request.json
    task = Task(
        subject=data['subject'],
        description=data['description'],
        hours=data['hours'],
        status="Pending"
    )
    db.session.add(task)
    db.session.commit()
    return jsonify({"message": "Task Added Successfully"})
**Retrieve Tasks API:**
@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([
        {
            "id": t.id,
            "subject": t.subject,
            "description": t.description,
            "hours": t.hours,
            "status": t.status
        } for t in tasks
    ])
**Frontend Implementation:**

The frontend interacts with backend APIs using JavaScript Fetch API.

**HTML Structure (Task Section):**
<div class="container">
    <h2>Add Study Task</h2>
    <input type="text" id="subject" placeholder="Subject">
    <input type="text" id="description" placeholder="Description">
    <input type="number" id="hours" placeholder="Hours">
    <button onclick="addTask()">Add Task</button>
</div>
**JavaScript API Call:**
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
    })
    .then(res => res.json())
    .then(data => alert(data.message));
}
**Installation and Setup:**

Clone the repository and navigate to the backend directory. Create a virtual environment if required, then install dependencies using the requirements file.

pip install -r requirements.txt

Run the Flask server:

python app.py

The server will start at:

http://127.0.0.1:5000

Open the frontend/index.html file in your browser to access the application.

**API Endpoints:**

The system exposes RESTful endpoints for adding tasks, retrieving tasks, recording marks, and viewing academic performance. All endpoints accept and return JSON data, enabling seamless client-server communication.

**Database Design:**

The application consists of two primary database models: Task and Performance. The Task model stores subject details, study hours, and completion status, while the Performance model records subject-wise academic marks. This relational design ensures structured data storage and efficient retrieval.

**Learning Outcomes:**

This project demonstrates full-stack web development skills including REST API design, CRUD operations using SQLAlchemy ORM, asynchronous frontend-backend integration, and structured project architecture. It highlights practical implementation of productivity and academic tracking systems.

**Future Enhancements:**

Future improvements may include authentication and authorization mechanisms, graphical analytics using chart libraries, study reminder notifications, Pomodoro timer integration, role-based dashboards, and cloud deployment for public access.

**Author:**
Developed by Madhumitha Ragavan https://github.com/MadhumithaRagavan

**License: **
This project is licensed under the [MIT License](LICENSE).
