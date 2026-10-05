def add_task(task_name, task_list=None):
    if task_list is None:
        task_list=[]
        
    task_list.append(task_name)
    print(task_list)

add_task("Read the book")
add_task("Send the letter")
add_task("Go to the gym")