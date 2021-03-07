import sqlite3


def delete_all_lists():
    conn = sqlite3.connect('todos_database.db')
    c = conn.cursor()

    print('')
    print('Please note that this will also delete all todos within all lists')
    condition = input('Are you sure you want to delete all records? [y/n] ')
    print('')

    if condition == 'y':
        c.execute('DELETE FROM todo_lists')
        c.execute('DELETE FROM todos')
        print('All todo lists deleted')
        print('')
        conn.commit()

    conn.close()
