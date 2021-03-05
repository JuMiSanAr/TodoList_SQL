from create_todo_list import add_new_todo_list as newList
from delete_todo_list import delete_new_todo_list as deleteList

print('Hello again!')

while True:
    print('What would you like to do?')
    print('0 - Exit application')
    print('1 - Create new todo list')
    print('2 - Delete existing todo list')
    print('')

    selected_option = input('Please introduce a row number in order to proceed: ')

    if selected_option == '0':
        print('Bye bye!')
        break

    elif selected_option == '1':
        newList()

    elif selected_option == '2':
        deleteList()

    else:
        print('Please introduce a valid number.')
        print('')
