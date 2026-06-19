"""
Task Manager (console version)
---------------------------------
Lets the user add, view, complete, and delete tasks in an
in-memory list. Tasks do not persist after closing the program.
"""

tasks = []
status_options = ["pending", "completed"]

while True:
    print("\n=== Task Manager ===\n")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as completed")
    print("4. Delete task")
    print("5. Exit")

    option = input("\nChoose an option: ")

    # Add a new task with "pending" status by default
    if option == "1":
        print("\nWhat task do you want to add?")
        task = input("Task: ")
        tasks.append({"name": task, "status": status_options[0]})
        
    # List all tasks with their number and status
    elif option == "2":
        print("\n=== Task List ===\n")
        for i, task in enumerate(tasks):
            print(f"{i + 1}. Name: {task['name']} - Status: {task['status']}")
        input("\nPress Enter to continue...")

    # Mark an existing task as completed, validating the entered number
    elif option == "3":
        print("\nWhich task do you want to mark as completed?")

        try:
            task_number = int(input("Task number: "))
        except ValueError:
            print("Please enter a valid number.")
            input("\nPress Enter to continue...")
            continue

        if 0 < task_number <= len(tasks):
            if tasks[task_number - 1]['status'] == status_options[0]:
                tasks[task_number - 1]['status'] = status_options[1]
                print(f"Task {tasks[task_number - 1]['name']} has been marked as completed")
            else:
                print("This task is already completed.")
                input("\nPress Enter to continue...")
        else:
            print("Invalid task number.")
            input("\nPress Enter to continue...")

    # Delete a task by its number, validating that it exists
    elif option == "4":
        print("\nWhich task do you want to delete?")
        try:
            task_number = int(input("Task number: "))
        except ValueError:
            print("Please enter a valid number.")
            input("\nPress Enter to continue...")
            continue

        if 0 < task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"Task {removed_task['name']} has been deleted.")
        else:
            print("Invalid task number.")
            input("\nPress Enter to continue...")

    elif option == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Please choose between 1 and 5.")
        input("\nPress Enter to continue...")