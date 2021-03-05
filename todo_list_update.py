import sqlite3

conn = sqlite3.connect('todos_database.db')

c = conn.cursor()


def update_todo_list():
    name = input('Type the name of the list you want to update: ')

    list = c.execute('''
        SELECT * 
        FROM todo_lists
        WHERE todo_list_name == ?
    ''', (name,)
              )

    print(list)
