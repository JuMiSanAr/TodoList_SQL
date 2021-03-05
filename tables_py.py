import sqlite3

conn = sqlite3.connect("todos_database.db")

c = conn.cursor()

# Table with all todos
c.execute('''CREATE TABLE todo_lists
(
    todo_list_id INTEGER PRIMARY KEY,
    todo_list_name TEXT UNIQUE NOT NULL,
    description TEXT
);
''')

# Table with the information about a single todo
c.execute('''
    CREATE TABLE todos
(
    todo_id INTEGER PRIMARY KEY,
    todo_name TEXT UNIQUE NOT NULL,
    created TEXT,
    todo_list_id TEXT UNIQUE NOT NULL,
    due TEXT,
    assignee TEXT,
    importance TEXT,
    comments TEXT
);
''')




