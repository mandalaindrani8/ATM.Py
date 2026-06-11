tasks = []

while True:
    print("\n===== TASK MANAGEMENT SYSTEM =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ").strip()

    if choice == "1":
        task = input("Enter task name: ").strip()
        if task:
            tasks.append({"name": task, "completed": False})
            print("Task added successfully!")
        else:
            print("Task name cannot be empty.")

    elif choice == "2":
        if not tasks:
            print("No tasks available.")
        else:
            print("\n--- Task List ---")
            for i, task in enumerate(tasks, start=1):
                status = "Completed" if task["completed"] else "Pending"
                print(f"{i}. {task['name']} [{status}]")

    elif choice == "3":
        if not tasks:
            print("No tasks available.")
        else:
            try:
                num = int(input("Enter task number to complete: "))
                if 1 <= num <= len(tasks):
                    tasks[num - 1]["completed"] = True
                    print("Task marked as completed.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == "4":
        if not tasks:
            print("No tasks available.")
        else:
            try:
                num = int(input("Enter task number to delete: "))
                if 1 <= num <= len(tasks):
                    deleted = tasks.pop(num - 1)
                    print(f"Deleted task: {deleted['name']}")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == "5":
        print("Thank you for using the Task Management System!")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 5.")