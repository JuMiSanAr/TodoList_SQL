import sqlite3
from Search.filter_by_list import filter_by_list
from Search.filter_by_todo_name import filter_by_todo_name


def filter_menu():
    conn = sqlite3.connect('todos_database.db')
    c = conn.cursor()

    while True:
        print('')
        print('How would you like to filter the information?')
        print('')
        print('0 - Back to main menu')
        print('')
        print('1 - By list')
        print('2 - By todo name')
        print('')

        selected_option = input('Please introduce a row number in order to proceed: ')
        print('')

        if selected_option == '0':
            print('')
            break

        elif selected_option == '1':
            filter_by_list()

        elif selected_option == '2':
            filter_by_todo_name()

        else:
            print('ERROR - Please introduce a valid number.')
            print('')

    conn.commit()
    conn.close()