from todo_list_create import add_new_todo_list as new_list
from todo_list_delete import delete_todo_list as delete_list
from todo_list_update import update_todo_list as update_list
from single_todo_create import add_new_todo as new_todo
from single_todo_delete import delete_todo
from single_todo_update import update_todo

print('')
print('Hello again!')
print('')

while True:
    print('What would you like to do?')
    print('')
    print('0 - Exit application')
    print('')
    print('1 - Create new list of todos')
    print('2 - Delete existing list')
    print('3 - Update existing list')
    print('')
    print('4 - Create new todo')
    print('5 - Delete existing todo')
    print('6 - Update existing todo')
    print('')

    selected_option = input('Please introduce a row number in order to proceed: ')

    if selected_option == '0':

        print('')
        print('Bye bye!')
        break

    elif selected_option == '1':
        new_list()

    elif selected_option == '2':
        delete_list()

    elif selected_option == '3':
        update_list()

    elif selected_option == '4':
        new_todo()

    elif selected_option == '5':
        delete_todo()

    elif selected_option == '6':
        update_todo()

    else:
        print('ERROR - Please introduce a valid number.')
        print('')
