import sqlite3


def print_all_todos_names():
    conn = sqlite3.connect('todos_database.db')
    c = conn.cursor()

    all_todos_names = c.execute('''
        SELECT todo_id, todo_name
        FROM todos
        ORDER BY todo_id
    ''')

    print('List of all current todos: ')
    print('')

    for todo in all_todos_names:
        print(f'{todo[0]} - {todo[1]}')

    print('')

    conn.close()