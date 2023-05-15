from flask import Flask, jsonify, render_template, request, redirect
import sqlite3
import os
from flask_cors import CORS

app = Flask(__name__) # Flask app instanciation 
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/': {'origins': '*'}})


# Redirect

@app.route('/')
def redirect_to_tasks():
    return redirect('/tasks')

@app.route('/tasks', methods=['GET'])
def get_all_tasks():
    conn = sqlite3.connect('tasks.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks")
    rows = cur.fetchall()
    tasks = []
    for row in rows:
        task = {
            'id': row[0],
            'title': row[1],
            'description': row[2],
            'due_date': row[3],
            'completed': bool(row[4])
            }
        tasks.append(task)
    conn.close()
    return render_template('index.html', tasks=tasks)

@app.route('/new_task', methods=['GET', 'POST'])
def new_task():
    if request.method == 'POST':
        title = request.form['newTaskTitle']
        description = request.form['newTaskDescription']
        due_date = request.form['newTaskDueDate']
        conn = sqlite3.connect('tasks.db')
        cur = conn.cursor()
        cur.execute("INSERT INTO tasks (title, description, due_date, completed) VALUES (?, ?, ?, ?)", (title, description, due_date, 0))
        conn.commit()
        conn.close()
        return redirect('/tasks')
    else:
        return render_template('new_task.html')



@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    conn = sqlite3.connect('tasks.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    conn.commit()
    conn.close()
    print("Task id:", task_id, "deleted!")
    return ('', 204)



if __name__ == '__main__':

    # create database if it doesnt exist
    if not os.path.exists('tasks.db'):
        conn = sqlite3.connect('tasks.db')
        cur = conn.cursor()
        cur.execute('''CREATE TABLE tasks 
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                due_date TEXT,
                completed INTEGER NOT NULL DEFAULT 0);''')
        conn.commit()
        conn.close()

    # localhost app
    app.run(host='0.0.0.0', port=5000, debug=False)
