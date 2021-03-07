import sqlite3
from print_todo_lists_details import print_all_todo_lists as print_lists


def filter_by_list():
    conn = sqlite3.connect('todos_database.db')
    c = conn.cursor()

    while True:
        keywords = input('Look for:')
        print('')

        filtered_info = list(c.execute('''
            SELECT *
            FROM todos 
            INNER JOIN todo_lists tl on todos.todo_list_id = tl.todo_list_id
            WHERE (tl.todo_list_name LIKE ? OR tl.description LIKE ?)
            ORDER BY tl.todo_list_id
            ''', (f'%{keywords}%', f'%{keywords}%')))

        info_length = len(filtered_info)

        if info_length == 0:
            print('No results found')
            print('')
        else:
            for index, ll in enumerate(filtered_info):
                if index == 0:
                    print(f'    - List "{ll[9]}":')
                    print('')
                if index > 0:
                    if ll[8] != filtered_info[index - 1][8]:
                        print(f'    - List "{ll[9]}":')
                        print('')

                print(f'Todo: {ll[1]}')
                print(f'Created: {ll[3]}')
                print(f'Due: {ll[4]}')
                print(f'Assignee: {ll[5]}')
                print(f'Importance: {ll[6]}')
                print(f'Comments: {ll[7]}')
                print('')

        condition = input('Would you like to make another filter by list? [y/n]: ')

        conn.commit()

        if condition == 'y':
            print('')
        else:
            break

    conn.close()
