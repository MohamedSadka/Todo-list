#planning the program
# start the program
# ask the user to enter the commands (add , remove , view , exit)
# make a loop to constantly display the program
# use the conditions 
# if the action == add > ask the user about the name of the task , then add it
# elif the actio == view > check if the list has items > if yes view them : else > print (not tasks found)
# elif the action == 'remove' > ask the user about the name of this task > if it's found > delete it and print that to the user..
# if there're no tasks in the lists > print (no tasks found)
# elif the action == 'exit' > break and start over
#else (which means the command is not one of the previous ones )> print(invalid command)



tasks = []

while True:
    user_action = input("Enter the command you want to execute (add, remove, view, exit): ").lower()

    if user_action == 'add':
        task = input("Enter the task you want to add: ")
        tasks.append(task)

    elif user_action == 'view':
        if not tasks:
            print("No tasks are found.")
        else:
            for task in tasks:
                print(task)

    elif user_action == 'remove':
        task_to_delete = input("Enter the task name you want to remove: ")
        if task_to_delete in tasks:
            tasks.remove(task_to_delete)
            print(f"'{task_to_delete}' has been removed from the tasks.")
        else:
            print("This task is not found.")

    elif user_action == 'exit':
        break

    else:
        print("Invalid command")
