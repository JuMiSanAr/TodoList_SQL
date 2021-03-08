import sqlite3
from datetime import datetime
from functools import reduce
from Print_helpers.print_todo_lists_details import print_all_todo_lists as lists_details


def add_new_todo():
    conn = sqlite3.connect('todos_database.db')
    c = conn.cursor()

    lists = list(c.execute('SELECT * FROM todo_lists'))

    if len(lists) == 0:
        print('')
        print('ERROR - There are no existing todo lists.')
        print('''
Since each todo needs to be included in a todo list, 
please create a new todo list to start using the application.''')
        print('')

    else:
        while True:
            print('')
            name = input('Select a name for your new todo (required): ')

            all_names = list(c.execute('SELECT todo_name FROM todos'))

            does_name_exist = reduce(lambda acc, ll: True if ll[0] == name else acc, all_names, False)

            if name != '' and not does_name_exist:
                break
            elif does_name_exist:
                print('')
                print('ERROR - This todo already exists')
            else:
                print('')
                print('ERROR - Name cannot be empty')

        print('')
        lists_details()

        lists_length = len(list(c.execute('''
            SELECT todo_list_id 
            FROM todo_lists
        ''')))

        while True:
            todo_list_input = input('Select the number of the list where this todo will be included (required): ')

            try:
                if todo_list_input != '' and 0 < int(todo_list_input) <= lists_length:
                    break
                else:
                    print('')
                    print('ERROR - This list doesn\'t exist')
                    print('')

            except ValueError:
                print('')
                print('Please introduce a valid number from the list')
                print('')

        print('')
        # INCLUDE FORMAT LIMITATIONS
        due = input('When is this task due? ')
        print('')
        assignee = input('Who is in charge of completing this task? ')
        print('')

        while True:
            importance = input('Assign a level of importance (1-10) to this task: ')

            try:
                if 0 < int(importance) <= 10:
                    break
                else:
                    print('')
                    print('The importance level can only be a number between 1 and 10')
                    print('')
            except ValueError:
                print('')
                print('Please introduce a valid number')
                print('')

        print('')
        comments = input('Introduce any comments / instructions regarding this task: ')
        print('')

        created_time = datetime.now().strftime("%d/%m/%Y %H:%M")

        c.execute('''
            INSERT INTO todos (todo_name, todo_list_id, created, due, assignee, importance, comments)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (name, todo_list_input, created_time, due, assignee, importance, comments)
                  )

        print(f'Task "{name}" created')
        print('')

        conn.commit()
    conn.close()
