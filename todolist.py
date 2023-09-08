
tasks = []
while True:
    while True:
        user_input = input("add or delete or list? ")
        if user_input.strip(): 
            break

    if user_input == "add":
        input_task = input("Enter task: ")
        tasks.append(input_task)
    elif user_input == "delete":
        input_task = input("Enter task: ")
        tasks.remove(input_task)
        if input_task in tasks:
                tasks.remove(input_task)
        else:
            print("Task not found.")
        print("Invalid input")
    elif user_input == "list":
        print("Tasks:")
        print(tasks)
    else:
        print("Invalid input")
