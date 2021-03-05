import sqlite3

conn = sqlite3.connect('todos_database.db')

c = conn.cursor()


def delete_new_todo_list():
    name = input('Type the name of the list you want to delete: ')

    if name == '':
        print('No input selected.')
        print('')
    else :
        confirmation = input('''Are you sure you want to delete this list? [y/n] ''')

        if confirmation == 'y' or confirmation == 'yes':
            c.execute('''
                DELETE
                FROM todo_lists
                WHERE todo_list_name == ?
                ''', (name,)
                      )
            conn.commit()
            print(f'List "{name}" deleted.')

        print('')
