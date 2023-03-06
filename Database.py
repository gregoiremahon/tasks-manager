import sqlite3


conn = sqlite3.connect('tasks.db')
print("Connected to tasks database")

conn.execute('''CREATE TABLE tasks
             (id INTEGER PRIMARY KEY,
             title TEXT NOT NULL,
             description TEXT,
             due_date TEXT,
             completed BOOLEAN);''')

