import sqlite3
from Print_helpers.print_todo_lists_details import print_all_todo_lists as lists_details


def update_todo_list():
    conn = sqlite3.connect('todos_database.db')

    c = conn.cursor()

    lists_length = len(list(c.execute('SELECT * FROM todo_lists')))

    if lists_length == 0:
        print('')
        print('There are no existing todo lists')
        print('Please create a new todo list to start using the application')
        print('')

    else:
        while True:
            lists_details()

            list_id = input('Type the number of the list you want to update: ')

            this_todo_list = c.execute('''
                SELECT * 
                FROM todo_lists
                WHERE todo_list_id == ?
            ''', (list_id,)
                          )

            try:
                list_arr = list(this_todo_list)
                condition = list_arr[0][1]

                print('')
                print('This is the information about this list: ')
                print(f'1 - Name: {list_arr[0][1]}')
                if list_arr[0][2] != '':
                    print(f'2 - Description: {list_arr[0][2]}')
                else:
                    print('2 - This todo list doesn\'t have a description')

            except IndexError:
                print('')
                print('ERROR - This list doesn\'t exist')
                continue

            print('')

            while True:
                field_to_update = input('Please introduce the number of the row you would like to update:  ')

                if field_to_update == '1':
                    new_name = input(f'Please insert a new name: ')

                    if new_name != '':
                        c.execute('''
                            UPDATE todo_lists
                            SET
                                todo_list_name = ?
                            WHERE todo_list_id == ?
                        ''', (new_name, list_id)
                                  )
                        break
                    else:
                        print('ERROR - Name field cannot be empty')
                        print('')

                elif field_to_update == '2':
                    new_desc = input(f'Please insert a new description: ')

                    c.execute('''
                        UPDATE todo_lists
                        SET
                            description = ?
                        WHERE todo_list_id == ?
                    ''', (new_desc, list_id)
                              )
                    break

                else:
                    print('ERROR - Invalid input')
                    print('')
                    continue

            conn.commit()

            print('')
            next_step = input('Would you like to do any other updates? [y/n] ')
            print('')

            if next_step == 'y':
                continue
            else:
                break

    conn.close()
