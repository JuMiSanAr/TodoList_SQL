import sqlite3
from print_todo_lists_details import print_all_todo_lists as lists_details


def delete_todo_list():
    conn = sqlite3.connect('todos_database.db')
    c = conn.cursor()

    lists_length = len(list(c.execute('SELECT * FROM todo_lists')))

    if lists_length == 0:
        print('')
        print('ERROR - There are no existing todo lists.')
        print('Please create a new todo list to start using the application.')
        print('')

    else:
        print(lists_details())

        name = input('Type the name of the list you want to delete: ')

        if name == '':
            print('ERROR - No input selected.')
            print('')
        else:
            confirmation = input('''Are you sure you want to delete this list? [y/n] ''')

            if confirmation == 'y' or confirmation == 'yes':
                c.execute('''
                    DELETE
                    FROM todo_lists
                    WHERE todo_list_name == ?
                    ''', (name,)
                          )

                print(f'List "{name}" deleted.')

            print('')

    conn.commit()
    conn.close()