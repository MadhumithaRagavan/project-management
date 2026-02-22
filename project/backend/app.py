
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# -------------------- MODELS --------------------

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

# -------------------- ROUTES --------------------

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

@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    result = []
    for task in tasks:
        result.append({
            "id": task.id,
            "subject": task.subject,
            "description": task.description,
            "hours": task.hours,
            "status": task.status
        })
    return jsonify(result)

@app.route('/add-marks', methods=['POST'])
def add_marks():
    data = request.json
    performance = Performance(
        subject=data['subject'],
        marks=data['marks']
    )
    db.session.add(performance)
    db.session.commit()
    return jsonify({"message": "Marks Added Successfully"})

@app.route('/performance', methods=['GET'])
def get_performance():
    performance = Performance.query.all()
    result = []
    for p in performance:
        result.append({
            "subject": p.subject,
            "marks": p.marks
        })
    return jsonify(result)
@app.route('/')
def home():
    return "Study Planner Backend is Running Successfully 🚀"

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
    