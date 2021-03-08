import sqlite3


def delete_all_todos():
    conn = sqlite3.connect('todos_database.db')
    c = conn.cursor()

    print('')
    condition = input('Are you sure you want to delete all todos from all lists? [y/n] ')
    print('')

    if condition == 'y':
        c.execute('DELETE FROM todos')
        print('All todos deleted')
        print('')

    conn.commit()
    conn.close()
