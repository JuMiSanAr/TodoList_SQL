from Todo_lists.todo_list_create import add_new_todo_list as new_list
from Todo_lists.todo_list_delete import delete_todo_list as delete_list
from Todo_lists.todo_list_update import update_todo_list as update_list
from Single_todos.single_todo_create import add_new_todo as new_todo
from Single_todos.single_todo_delete import delete_todo
from Single_todos.single_todo_update import update_todo
from Delete_all.delete_all_lists import delete_all_lists as delete_lists
from Delete_all.delete_all_todos import delete_all_todos as delete_todos
from Delete_all.delete_todos_in_list import delete_todos_in_list
from Search.search_menu import filter_menu

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
    print('7 - Delete all lists')
    print('8 - Delete all todos')
    print('9 - Delete all todos in a list')
    print('')
    print('10 - Filter todos')
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

    elif selected_option == '7':
        delete_lists()

    elif selected_option == '8':
        delete_todos()

    elif selected_option == '9':
        delete_todos_in_list()

    elif selected_option == '10':
        filter_menu()

    else:
        print('ERROR - Please introduce a valid number.')
        print('')
