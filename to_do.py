def add_task():
    
    with open ('todo.txt', 'a') as file:
        to_do_list = {}
        to_do_list['task'] = input('Enter a task.')
        to_do_list['due date'] = input('Enter a a due date yyyy/mm/dd.')
        to_do_list['priority'] = input('Enter a priority level low/normal/high.')
        file.write(str(to_do_list)+'\n')
        
def show_list():
    
    with open('todo.txt', 'r') as file:
        tasks = file.readlines()
        for i in tasks:
            print(eval(i))
          
def mark_as_done():
    
    with open ('todo.txt', 'r') as file:
        tasks = file.readlines()
        task = input('Which task would you like to mark as complete: ')
        to_do_list = []
        for i in tasks:
            to_do_list.append(eval(i))
        for i in to_do_list:
            if i['task'] == task:
                i['status'] = 'done'
        with open ('todo.txt', 'w') as file:
            for i in to_do_list:
                file.write(str(i) + '\n')
        
mark_as_done()              
# add_task()
show_list()