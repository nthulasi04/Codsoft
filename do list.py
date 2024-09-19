to_do_list = []

while True:
    user_input = input("Enter a command (create, update, delete, or list): ")

    if user_input == "create":
        task = input("Enter a new task: ")
        to_do_list.append(task)
        print("Task added successfully!")

    elif user_input == "update":
        task_index = int(input("Enter the task index: "))
        new_task = input("Enter the new task description: ")
        to_do_list[task_index - 1] = new_task
        print("Task updated successfully!")

    elif user_input == "delete":
        task_index = int(input("Enter the task index: "))
        del to_do_list[task_index - 1]
        print("Task deleted successfully!")

    elif user_input == "list":
        print("To-Do List:")
        for i, task in enumerate(to_do_list, start=1):
            print(f"{i}. {task}")

    else:
        print("Invalid command. Please try again!")