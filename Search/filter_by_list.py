import sqlite3


def filter_by_list():
    conn = sqlite3.connect('todos_database.db')
    c = conn.cursor()

    while True:
        keywords = input('Look for: ')
        print('')

        filtered_info = list(c.execute('''
            SELECT *
            FROM todo_lists tl
            LEFT JOIN todos on todos.todo_list_id = tl.todo_list_id
            WHERE (tl.todo_list_name LIKE ? OR tl.description LIKE ?)
            ORDER BY tl.todo_list_id
            ''', (f'%{keywords}%', f'%{keywords}%')))

        info_length = len(filtered_info)

        if info_length == 0:
            print('No results found')
            print('')
        else:
            for index, ll in enumerate(filtered_info):

                if index > 0:
                    if ll[0] != filtered_info[index - 1][0]:
                        print(f'    - List "{ll[1]}":')
                        print('')
                else:
                    print(f'    - List "{ll[1]}":')
                    print('')

                if ll[4]:
                    print(f'Todo: {ll[4]}')
                    print(f'Created: {ll[6]}')
                    print(f'Due: {ll[7]}')
                    print(f'Assignee: {ll[8]}')
                    print(f'Importance: {ll[9]}')
                    print(f'Comments: {ll[10]}')
                    print('')
                else:
                    print('There are no todos in this list')
                    print('')

            conn.commit()

        condition = input('Would you like to make another filter by list? [y/n]: ')

        if condition == 'y':
            print('')
        else:
            break

    conn.close()
