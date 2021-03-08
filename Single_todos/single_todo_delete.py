import sqlite3
from Print_helpers.print_todos_names import print_all_todos_names as print_todos


def delete_todo():

    conn = sqlite3.connect('todos_database.db')
    c = conn.cursor()

    lists_length = len(list(c.execute('SELECT * FROM todos')))

    print('')

    if lists_length == 0:

        print('ERROR - There are no existing todos')
        print('Please create a new todo to start organizing your tasks')
        print('')

    else:
        print_todos()

        id_to_delete = input('Type the number of the todo that you want to delete: ')

        if id_to_delete == '':
            print('ERROR - No input selected.')
            print('')
        else:
            confirmation = input('''Are you sure you want to delete this todo? [y/n] ''')

            if confirmation == 'y' or confirmation == 'yes':

                name = list(c.execute('SELECT todo_name FROM todos WHERE todo_id == ? ', (id_to_delete,)))

                c.execute('''
                    DELETE
                    FROM todos
                    WHERE todo_id == ?
                    ''', (id_to_delete,)
                          )

                print(f'Todo "{name[0][0]}" deleted.')

            print('')

            conn.commit()

    conn.close()
