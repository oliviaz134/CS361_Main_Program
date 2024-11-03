
def display_navigation_menu():
    print('Navigation Menu\n\n\
    1. View Instructions\n\
    2. View To-Dos List\n\
    0. Quit')
    
    nav_input = input('Enter \'2\' to go to your To-Dos List to start adding To-Dos or another number from the Navigation Menu: ')

    if nav_input.strip() == '1':
        display_instructions()
    elif nav_input.strip() == '2':
        display_todos_list(current_todos, completed_todos)
    elif nav_input.strip() == '0':
        quit()
    else:
        print('Invalid command.')
    return

def display_instructions():
    print('**********\nInstructions\n\
    This To-Do application is a simple way to track and complete your tasks. Listed below are the available functionalities in the To-Do application.\n\n\
    View To-Dos List: allows you to view your current, in-progress To-Dos, as well as your completed To-Dos.\n\
    Add a To-Do: allows you to add a new To-Do to your To-Dos list.\n\
    Complete a To-Do: allows you to mark a To-Do as complete, and will move the To-Do to the Completed Section.\n\
    Delete a To-Do: allows you to permanently delete a To-Do from your To-Dos list.\n**********')
    user_input = input('Enter \'M\' to view the Navigation Menu: ')
    print('**********')

    if user_input.strip().capitalize() == 'M':
        display_navigation_menu()
    else:
        print('Invalid command.')
        display_instructions()
    return

def display_todos_list(current_todos, completed_todos):
    print('**********\nTo-Dos List')

    for i, todo in enumerate(current_todos):
        print(f'ID: {i} {todo}')
    
    print('\nCompleted')

    for i, todo in enumerate(completed_todos):
        print(f'{todo}')
    
    print('\nActions:\n\
    A. Add a To-Do\n\
    C. Complete a To-Do\n\
    D. Delete a To-Do\n')

    action_input = input('Enter one of the letters from the Actions menu to perform an action or \'M\' to view the Navigation Menu: ').strip().capitalize()

    if action_input.strip().capitalize() == 'M':
        display_navigation_menu()
    elif action_input.strip().capitalize() == 'A':
        add_todo(current_todos)
    elif action_input.strip().capitalize() == 'C':
        current_todos, completed_todos = complete_todo(current_todos, completed_todos)
    elif action_input.strip().capitalize() == 'D':
        current_todos = delete_todo(current_todos)
    else:
        print('Invalid command.')
    display_todos_list(current_todos, completed_todos)

def add_todo(current_todos):
    print('Add a To-Do\n')
    description = input('Description: ')

    action_input = input('Enter \'Y\' to add the new To-Do to your To-Dos list, \'N\' to cancel, or \'M\' to return to the Navigation Menu: ')

    if action_input.strip().capitalize() == 'M':
        display_navigation_menu()
    elif action_input.strip().capitalize() == 'Y':
        current_todos.append(description)
        return
    elif action_input.strip().capitalize() == 'N':
        return
    else:
        print('Invalid command.')

def complete_todo(current_todos, completed_todos):
    print('**********\nComplete a To-Do')
    todo_id = int(input('Type in the To-Do ID you\'d like to mark as complete: '))

    action_input = input('Enter \'Y\' to complete the To-Do, \'N\' to cancel, or \'M\' to return to the Navigation Menu: ')

    if action_input.strip().capitalize() == 'M':
        display_navigation_menu()
    elif action_input.strip().capitalize() == 'Y':
        todo_to_complete = None
        for i, todo in enumerate(current_todos):
            if i == todo_id:
                todo_to_complete = todo
            
        if todo_to_complete is not None:
            current_todos.pop(todo_id)
            completed_todos.append(todo_to_complete)
            return current_todos, completed_todos
        else:
            print('To-Do ID does not exist.')
            complete_todo(current_todos, completed_todos)
    elif action_input.strip().capitalize() == 'N':
        return current_todos, completed_todos
    else:
        print('Invalid command.')

def delete_todo(current_todos):
    print('**********\nDelete a To-Do')
    todo_id = int(input('Type in the To-Do ID you\'d like to delete: '))

    action_input = input('Enter \'Y\' to continue, \'N\' to cancel, or \'M\' to return to the Navigation Menu: ')

    if action_input.strip().capitalize() == 'M':
        display_navigation_menu()
    elif action_input.strip().capitalize() == 'Y':
        secondary_action_input = input('Are you sure you want to delete this To-Do?\n*Deleting this To-Do will permanently remove the To-Do data*\nEnter \'Y\' to confirm, \'N\' to cancel, or \'M\' to return to the Navigation Menu: ')

        if secondary_action_input.strip().capitalize() == 'M':
            display_navigation_menu()
        elif secondary_action_input.strip().capitalize() == 'Y':
            todo_deleted = False
            for i in range(len(current_todos)):
                if i == todo_id:
                    current_todos.pop(i)
                    todo_deleted = True
            
            if todo_deleted:
                return current_todos
            else:
                print('To-Do ID does not exist.')
                delete_todo(current_todos)
        elif secondary_action_input.strip().capitalize() == 'N':
            return current_todos
        else:
            print('Invalid command.')
    elif action_input.strip().capitalize() == 'N':
        return current_todos
    else:
        print('Invalid command.')

if __name__ == '__main__':
    app_is_running = True
    current_todos = []
    completed_todos = []
    # current_todos = ['walk the dog', 'feed the cat']
    # completed_todos = ['take out the trash']

    while app_is_running:
        print('To-Do Application\n')
        display_navigation_menu()
