import sqlite3

conn = sqlite3.connect('todos_database.db')

c = conn.cursor()


def add_new_todo_list():
    name = input('Select a name for your new todo list: ')
    print('Add a description for your todo list.')
    desc = input('If you do not want to add a description, leave this field empty: ')

    c.execute('''
        INSERT INTO todo_lists (todo_list_name, description)
        VALUES (?, ?)
        ''', (name, desc)
              )

    conn.commit()
    print(f'List "{name}" created')
    print('')
