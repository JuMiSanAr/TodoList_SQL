import sqlite3
from Search.filter_by_list import filter_by_list


def filter_menu():
    conn = sqlite3.connect('todos_database.db')
    c = conn.cursor()

    while True:
        print('How would you like to filter the information?')
        print('')
        print('0 - Back to main menu')
        print('')
        print('1 - By list')
        print('')

        selected_option = input('Please introduce a row number in order to proceed: ')

        if selected_option == '0':
            print('')
            break

        elif selected_option == '1':
            filter_by_list()

        else:
            print('ERROR - Please introduce a valid number.')
            print('')

    conn.commit()
    conn.close()