from todo_list_create import add_new_todo_list as new_list
from todo_list_delete import delete_new_todo_list as delete_list
from todo_list_update import update_todo_list as update_list

print('Hello again!')

while True:
    print('What would you like to do?')
    print('0 - Exit application')
    print('1 - Create new todo list')
    print('2 - Delete existing todo list')
    print('3 - Update existing todo list')
    print('')

    selected_option = input('Please introduce a row number in order to proceed: ')

    if selected_option == '0':
        print('Bye bye!')
        break

    elif selected_option == '1':
        new_list()

    elif selected_option == '2':
        delete_list()

    elif selected_option == '3':
        update_list()

    else:
        print('Please introduce a valid number.')
        print('')
