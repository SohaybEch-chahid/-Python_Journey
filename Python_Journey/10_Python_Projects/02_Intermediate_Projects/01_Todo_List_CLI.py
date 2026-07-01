tasks = []

while True:
    print("\n=== Todo List ===")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        task = input("Task: ")
        tasks.append(task)

    elif choice == "2":
        if not tasks:
            print("No tasks.")
        else:
            for index, task in enumerate(tasks, start=1):
                print(f"{index} --> {task}")

    elif choice == "3":
        for index, task in enumerate(tasks, start=1):
            print(f"{index} --> {task}")

        number = int(input("Task number to delete: "))

        if 1 <= number <= len(tasks):
            tasks.pop(number - 1)
        else:
            print("Not found this task, is invalid choice.")

    elif choice == "4":
        break

    else:
        print("Invalid choice.")
