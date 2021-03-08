import sqlite3
from Print_helpers.print_todo_lists_details import print_all_todo_lists as lists_details


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
        lists_details()

        list_id = input('Type the name of the list you want to delete: ')

        if list_id == '':
            print('ERROR - No input selected.')
            print('')
        else:
            confirmation = input('''Are you sure you want to delete this list? [y/n] ''')

            if confirmation == 'y' or confirmation == 'yes':

                name = list(c.execute('SELECT todo_list_name FROM todo_lists WHERE todo_list_id == ? ', (list_id,)))

                c.execute('''
                    DELETE
                    FROM todo_lists
                    WHERE todo_list_id == ?
                    ''', (list_id,)
                          )

                print(f'List "{name[0][0]}" deleted.')

            print('')

    conn.commit()
    conn.close()
