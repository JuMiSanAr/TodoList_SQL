import sqlite3

conn = sqlite3.connect('todos_database.db')

c = conn.cursor()


def print_all_todo_lists():
    todo_lists = c.execute('''
            SELECT * 
            FROM todo_lists
            ORDER BY todo_list_id
        ''')

    print('List of all current todo lists: ')
    print('')

    for ll in todo_lists:
        print(f'{ll[0]} - Name: {ll[1]}')
        if ll[2] != '':
            print(f'Description: {ll[2]}')
        else:
            print('This todo list doesn\'t have a description')
        print('')
