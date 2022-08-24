from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

@app.before_first_request
def create_tables():
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description text,
        done bool
    )""")
    conn.commit()
    conn.close()

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/tasks")
def tasks():
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
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    description = request.form["description"]
    c.execute("INSERT INTO tasks (description, done) VALUES (?, ?)", (description, 0))
    conn.commit()
    conn.close()
    return "Success"

if __name__ == "__main__":
    app.run()
