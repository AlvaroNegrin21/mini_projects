"""
Task Manager (with persistence)
-----------------------------------
Same as task_manager, but tasks are saved to a tasks.json file
and loaded automatically on startup, so they aren't lost when
the program closes.
"""

from tasks import add_task, view_tasks, mark_task_completed, delete_task, save_tasks, load_tasks

tasks = load_tasks()
 
while True:
    print("\n=== Task Manager ===\n")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as completed")
    print("4. Delete task")
    print("5. Exit")
    
    option = input("\nChoose an option: ")
    
    if option == "1":
        add_task(tasks)
        save_tasks(tasks)
    elif option == "2":
        view_tasks(tasks)
    elif option == "3":
        mark_task_completed(tasks)
        save_tasks(tasks)
    elif option == "4":
        delete_task(tasks)
        save_tasks(tasks)
    elif option == "5":
        print("Exiting the task manager...")
        break
    else:
        print("Invalid option. Please choose a valid one.")