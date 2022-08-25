from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)


@app.before_first_request
def create_tables():
    """Create the database table if it doesn't exist."""
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description text,
        done bool
    c.execute("SELECT * FROM tasks")
    tasks = c.fetchall()
    if len(tasks) == 0:
        c.execute("INSERT INTO tasks (description, done) VALUES (:description, :done)",
                  {"description": "Task 1", "done": 0})
        c.execute("INSERT INTO tasks (description, done) VALUES (:description, :done)",
                  {"description": "Task 2", "done": 0})
        c.execute("INSERT INTO tasks (description, done) VALUES (:description, :done)",
                  {"description": "Task 3", "done": 0})
    )""")
    conn.commit()
    conn.close()


@app.route("/")
def hello():
    """Test route."""
    return "Hello World!"


@app.route("/tasks")
def tasks():
    """Get all tasks."""
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute("SELECT * FROM tasks")
    tasks = c.fetchall()
    tasks_list = []
    for task in tasks:
        tasks_list.append({
            "id": task[0],
            "description": task[1],
            "done": task[2]
        })
    return jsonify(tasks_list)


@app.route("/add", methods=["POST"])
def add():
    """Add a task."""
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    description = request.form["description"]
    c.execute("INSERT INTO tasks (description, done) VALUES (:description, :done)",
              {"description": description, "done": 0})
    conn.commit()
    conn.close()
    return str(c.lastrowid)


@app.route("/update", methods=["POST"])
def update():
    """Update a task."""
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    id = request.form["id"]
    description = request.form["description"]
    done = request.form["done"]
    c.execute("UPDATE tasks SET description = ?, done = ? WHERE id = ?", (description, done, id))
    conn.commit()
    conn.close()
    return "Success"


if __name__ == "__main__":
    app.run()
