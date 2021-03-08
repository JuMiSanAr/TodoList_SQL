import sqlite3


def filter_by_todo_name():
    conn = sqlite3.connect('todos_database.db')
    c = conn.cursor()

    while True:
        keywords = input('Look for: ')
        print('')

        filtered_info = list(c.execute('''
               SELECT *
               FROM todos 
               INNER JOIN todo_lists tl on todos.todo_list_id = tl.todo_list_id
               WHERE todos.todo_name LIKE ?
               ORDER BY todos.todo_name
               ''', (f'%{keywords}%',)))

        for todo in filtered_info:
            print(f'Todo "{todo[1]}"')
            print(f'In list: {todo[9]}')
            print(f'Created: {todo[3]}')
            print(f'Due: {todo[4]}')
            print(f'Assignee: {todo[5]}')
            print(f'Importance: {todo[6]}')
            print(f'Comments: {todo[7]}')

            print('')

        conn.commit()

        condition = input('Would you like to make another filter by todo name? [y/n]: ')

        if condition == 'y':
            print('')
        else:
            break

    conn.close()
