from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response


@app.before_first_request
def create_tables():
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT,
        done BOOLEAN
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
    tasks = []
    for row in c.fetchall():
        tasks.append({
            "id": row[0],
            "description": row[1],
            "done": row[2]
        })
    return jsonify(tasks)


@app.route("/add", methods=["POST"])
def add():
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute("INSERT INTO tasks (description, done) VALUES (?, ?)", (request.form["description"], 0))
    c.execute("SELECT id FROM tasks ORDER BY id DESC LIMIT 1")
    id = c.fetchone()[0]
    conn.commit()
    conn.close()
    return "OK"


@app.route("/update", methods=["POST"])
def update():
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute("UPDATE tasks SET description = ?, done = ? WHERE id = ?", (request.form["description"], request.form["done"], request.form["id"]))
    conn.commit()
    conn.close()
    return "OK"


if __name__ == "__main__":
    app.run()
