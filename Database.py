from flask import Flask, jsonify, render_template, request, redirect
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

@app.route('/new_task', methods=['GET', 'POST']) # Route for GET/POST requests on new_task page
def new_task():
    if request.method == 'POST':
        # récupération des données envoyées depuis le formulaire
        title = request.form['title']
        description = request.form['description']
        due_date = request.form['due_date']

        # insertion des données dans la base de données
        conn = sqlite3.connect('tasks.db')
        cur = conn.cursor()
        cur.execute("INSERT INTO tasks (title, description, due_date) VALUES (?, ?, ?)", (title, description, due_date))
        conn.commit()
        conn.close()

        # redirection vers la page d'accueil
        return redirect('/')
    else:
        return render_template('new_task.html')


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
