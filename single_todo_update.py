import sqlite3
from print_todos_names import print_all_todos_names as print_todos
from print_todo_lists_details import print_all_todo_lists as print_lists


def update_todo():
    conn = sqlite3.connect('todos_database.db')
    c = conn.cursor()

    todos_length = len(list(c.execute('SELECT * FROM todos')))

    if todos_length == 0:
        print('')
        print('ERROR - There are no existing todos')
        print('Please create a new todo to start organizing your tasks')
        print('')

    else:
        while True:
            print('')

            print_todos()

            todo_id = input('Type the number of the todo you want to update: ')

            todo = c.execute('''
                SELECT * 
                FROM todos
                WHERE todo_id == ?
            ''', (todo_id,)
                          )

            try:
                todo_arr = list(todo)
                condition = todo_arr[0][1]

                print('')
                print('This is the information about this todo: ')
                print('')
                print(f'1 - Name: {todo_arr[0][1]}')

                corresponding_todo_list = list(c.execute('''
                    SELECT todo_list_name
                    FROM todo_lists
                    WHERE todo_list_id == ?
                ''', (todo_arr[0][0],)
                ))

                print(f'2 - Within list: {corresponding_todo_list[0][0]}')

                if todo_arr[0][4] != '':
                    print(f'3 - Due: {todo_arr[0][4]}')
                else:
                    print('3 - This todo list doesn\'t have a due date')

                if todo_arr[0][5] != '':
                    print(f'4 - Assignee: {todo_arr[0][5]}')
                else:
                    print('4 - This todo list doesn\'t have an assignee')

                if todo_arr[0][6] != '':
                    print(f'5 - Importance: {todo_arr[0][6]}')
                else:
                    print('5 - This todo list doesn\'t have a determined level of importance')

                if todo_arr[0][7] != '':
                    print(f'6 - Comments: {todo_arr[0][7]}')
                else:
                    print('6 - This todo list doesn\'t have any comments')

                print('')

            except IndexError:
                print('')
                print('ERROR - This todo doesn\'t exist')
                continue

            while True:
                field_to_update = input('Please introduce the number of the row you would like to update:  ')

                print('')

                if field_to_update == '1':
                    while True:
                        new_name = input(f'Please insert a new name: ')

                        if new_name != '':
                            c.execute('''
                                UPDATE todos
                                SET todo_name = ?
                                WHERE todo_id == ?
                            ''', (new_name, todo_id)
                                      )
                            break
                        else:
                            print('')
                            print('ERROR - Name field cannot be empty')
                            print('')

                elif field_to_update == '2':
                    while True:
                        print_lists()

                        new_list = input(f'Please insert a new list for this todo: ')

                        if new_list != '':
                            c.execute('''
                                UPDATE todos
                                SET
                                    todo_list_id = ?
                                WHERE todo_id == ?
                            ''', (new_list, todo_id)
                                      )
                            break
                        else:
                            print('')
                            print('ERROR - List field cannot be empty')
                            print('')

                elif field_to_update == '3':
                    new_due = input(f'Please insert a new due date and time for this todo: ')

                    c.execute('''
                        UPDATE todos
                        SET due = ?
                        WHERE todo_id == ?
                    ''', (new_due, todo_id)
                              )
                    break

                else:
                    print('ERROR - Invalid input')
                    print('')
                    continue

            conn.commit()

            print('')
            next_step = input('Would you like to do any other updates? [y/n] ')

            if next_step == 'y':
                continue
            else:
                break

    conn.close()
