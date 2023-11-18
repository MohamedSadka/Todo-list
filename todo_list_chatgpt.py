def add_task(tasks):
    task = input("Enter the task you want to add: ")
    tasks.append(task)

def view_tasks(tasks):
    if not tasks:
        print("No tasks are found.")
    else:
        for task in tasks:
            print(task)

def remove_task(tasks):
    task_to_delete = input("Enter the task name you want to remove: ")
    if task_to_delete in tasks:
        tasks.remove(task_to_delete)
        print(f"'{task_to_delete}' has been removed from the tasks.")
    else:
        print("This task is not found.")

tasks = []

while True:
    user_action = input("Enter the command you want to execute (add, remove, view, exit): ").lower()

    if user_action == 'add':
        add_task(tasks)

    elif user_action == 'view':
        view_tasks(tasks)

    elif user_action == 'remove':
        remove_task(tasks)

    elif user_action == 'exit':
        break

    else:
        print("Invalid command")
