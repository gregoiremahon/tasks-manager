from flask import Flask, jsonify, render_template
import sqlite3
import os

app = Flask(__name__) # Flask app instanciation 

@app.route('/tasks', methods=['GET']) # Route for GET request on webapp
def get_all_tasks():
    conn = sqlite3.connect('tasks.db') # Connect to SQLite3 database
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks") ## SELECT all lines in tasks database table
    rows = cur.fetchall() # Gets all lines from previous query

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
    #return jsonify(tasks) ## returns all tasks in json format
    return render_template('index.html', tasks=tasks)
if __name__ == '__main__':
    # create database if it doesnt exist
    if not os.path.exists('tasks.db'):
        conn = sqlite3.connect('tasks.db')
        cur = conn.cursor()
        cur.execute('''CREATE TABLE tasks 
                (id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                description TEXT,
                due_date TEXT,
                completed INTEGER NOT NULL DEFAULT 0);''')
        conn.commit()
        conn.close()
    # localhost app
    app.run(port=5000, debug=False)
