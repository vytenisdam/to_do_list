from datetime import date

def add_task():
    '''Adds a task to a file.'''   
    with open ('todo.txt', 'a') as file:
        to_do_list = {}
        to_do_list['task'] = input('Enter a task name:').lower()
        to_do_list['priority'] = input('Enter a priority level low/normal/high: ').lower()
        to_do_list['creation date'] = str(date.today())
        to_do_list['due date'] = input('Enter a a due date yyyy-mm-dd: ')
        to_do_list['status'] = 'to do'
        to_do_list['notes'] = input('Enter your notes regarding task: ').lower()
        file.write(str(to_do_list)+'\n')
        
def show_list():
    '''Shows all tasks.'''
    with open('todo.txt', 'r') as file:
        tasks = file.readlines()
        for i in tasks:
            print(eval(i))
          
def mark_as_done():
    '''Marks specified task as done'''
    with open ('todo.txt', 'r') as file:
        tasks = file.readlines()
        task = input('Which task would you like to mark as complete: ').lower()
        to_do_list = []
        for i in tasks:
            to_do_list.append(eval(i))
        for i in to_do_list:
            if i['task'] == task:
                i['status'] = 'done'
        with open ('todo.txt', 'w') as file:
            for i in to_do_list:
                file.write(str(i) + '\n')

def update_task():
    '''Updates selected task and selected attribute'''
    task = input('Which task would you like to update? ').lower()
    attribute = input('Which attribute: ').lower()
    with open ('todo.txt', 'r') as file:
        tasks = file.readlines()
        to_do_list = []
        for i in tasks:
            to_do_list.append(eval(i))
        for i in to_do_list:
            if i['task'] == task:
                to_do_list[to_do_list.index(i)][attribute] = input('Type your change: ').lower()
        with open ('todo.txt', 'w') as file:
            for i in to_do_list:
                file.write(str(i) + '\n')
                
def view_tasks():
    '''View tasks by date creation or due.'''
    view = input("If you would like to see tasks by creation date, type - 'creation date', if by due date, type 'due date' ").lower()
    date = input('Which date interests you type in format yyyy-mm-dd: ')
    with open('todo.txt', 'r') as file:
        to_do_list = []
        tasks = file.readlines()
        for i in tasks:
            to_do_list.append(eval(i))
        right_tasks = []
        for i in to_do_list:
            if i[view] == date:
                right_tasks.append(i)
        for i in right_tasks:
            print(i)
                        
def delete_task():
    '''Deletes selected task.'''
    deletion = input('Which task would you like to delete? ').lower()
    with open('todo.txt', 'r') as file:
        tasks = file.readlines()
        to_do_list = []
        for i in tasks:
            to_do_list.append(eval(i))
        for i in to_do_list:
            if i['task'] == deletion:
                to_do_list.pop(to_do_list.index(i))
        with open('todo.txt', 'w') as file:
            for i in to_do_list:
                file.write(str(i) + '\n')
                
def view_tasks_due_today():
    '''Shows all tasks due today.'''
    with open('todo.txt', 'r') as file:
        to_do_list = []
        tasks = file.readlines()
        for i in tasks:
            to_do_list.append(eval(i))
        today_tasks = []
        for i in to_do_list:
            if i['due date'] == str(date.today()):
                today_tasks.append(i)
        for i in today_tasks:
            print("Here's the tasks, due today: ")
            print(i)
                                
def main():
    
    view_tasks_due_today()
    choice = input("What would you like to do?\n Add task, type - 'add',\n Delete task, type - 'del',\n See all tasks in list, type - 'see',\n Update a task, type -'update',\n Mark task as done, type - 'done',\n View tasks by date, type - 'view': ").lower()
    if choice == 'add':
        add_task()
    elif choice == 'del':
        delete_task()
    elif choice == 'see':
        show_list()
    elif choice == 'update':
        update_task()
    elif choice == 'done':
        mark_as_done()
    elif choice == 'view':
        view_tasks()
        
main()