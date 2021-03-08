import sqlite3
from Print_helpers.print_todo_lists_details import print_all_todo_lists as print_lists


def delete_todos_in_list():
    conn = sqlite3.connect('todos_database.db')
    c = conn.cursor()

    print('')
    print_lists()

    selected_list = input('Please introduce the number of the list that you want to empty out: ')

    selected_list_name = list(c.execute(''' SELECT todo_list_name 
                                            FROM todo_lists 
                                            WHERE todo_list_id == ?''',
                                        (selected_list,)))

    print('')
    condition = input(f'Are you sure that you want to delete all todos from list {selected_list_name[0][0]}? [y/n] ')
    print('')

    if condition == 'y':
        c.execute('DELETE FROM todos WHERE todo_list_id == ?', (selected_list,))

        print(f'All todos from list "{selected_list_name[0][0]}" deleted')
        print('')
        conn.commit()

    conn.close()
