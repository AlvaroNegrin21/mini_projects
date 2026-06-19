"""
Task manager functions: add, view, complete, delete, and
persist tasks in a JSON file.
"""

import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_FILE = os.path.join(BASE_DIR, "tasks.json")


def add_task(task_list):
    """Asks the user for a task name and appends it to the list with 'pending' status.

    Args:
        task_list (list): list of tasks to append the new one to.
    """
    print("\nWhat task do you want to add?")
    task = input("Task: ")
    task_list.append({"name": task, "status": "pending"})


def view_tasks(task_list):
    """Displays all tasks with their number and status.

    Args:
        task_list (list): list of tasks to display.
    """
    print("\n=== Task List ===\n")
    for i, task in enumerate(task_list):
        print(f"{i + 1}. Name: {task['name']} - Status: {task['status']}")
    input("\nPress Enter to continue...")


def mark_task_completed(task_list):
    """Asks for a task number and marks it as 'completed' if it's pending.

    Args:
        task_list (list): list of tasks to apply the change to.
    """
    print("\nWhich task do you want to mark as completed?")

    try:
        task_number = int(input("Task number: "))
    except ValueError:
        print("Please enter a valid number.")
        input("\nPress Enter to continue...")
        return

    if 0 < task_number <= len(task_list):
        if task_list[task_number - 1]['status'] == "pending":
            task_list[task_number - 1]['status'] = "completed"
            print(f"Task {task_list[task_number - 1]['name']} has been marked as completed")
            input("\nPress Enter to continue...")
        else:
            print("This task is already completed.")
            input("\nPress Enter to continue...")
    else:
        print("Invalid task number.")
        input("\nPress Enter to continue...")


def delete_task(task_list):
    """Asks for a task number and removes it from the list.

    Args:
        task_list (list): list of tasks to remove one from.
    """
    print("\nWhich task do you want to delete?")
    try:
        task_number = int(input("Task number: "))
    except ValueError:
        print("Please enter a valid number.")
        input("\nPress Enter to continue...")
        return
    if 0 < task_number <= len(task_list):
        removed_task = task_list.pop(task_number - 1)
        print(f"Task {removed_task['name']} has been deleted.")
    else:
        print("Invalid task number.")
        input("\nPress Enter to continue...")

        
def save_tasks(task_list, filename=DEFAULT_FILE):
    """Saves the list of tasks to a JSON file.

    Args:
        task_list (list): list of tasks to save.
        filename (str): path of the file to save to. Defaults to tasks.json.
    """
    with open(filename, "w") as file:
        json.dump(task_list, file)

        
def load_tasks(filename=DEFAULT_FILE):
    """Loads the list of tasks from a JSON file.

    Args:
        filename (str): path of the file to load. Defaults to tasks.json.

    Returns:
        list: loaded list of tasks, or empty list if the file doesn't exist.
    """
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []