import sqlite3


def add_new_todo_list():
    conn = sqlite3.connect('todos_database.db')
    c = conn.cursor()

    print('')
    name = input('Select a name for your new todo list: ')
    print('')
    print('Add a description for your todo list.')
    desc = input('If you do not want to add a description, leave this field empty: ')

    c.execute('''
        INSERT INTO todo_lists (todo_list_name, description)
        VALUES (?, ?)
        ''', (name, desc)
              )

    print(f'List "{name}" created')
    print('')

    conn.commit()
    conn.close()
