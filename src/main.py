#!/usr/bin/env python3

import sys
from task import Task
from manager import TaskManager

def print_usage():
    print("\nTo-Do List Application")
    print("Available commands:")
    print("  add       - Add a new task")
    print("  list      - List all tasks")
    print("  complete  - Mark a task as complete")
    print("  delete    - Delete a task")
    print("  quit      - Exit the application\n")

def main():
    manager = TaskManager()
    
    while True:
        command = input("Enter command (or 'help' for usage): ").strip().lower()
        
        if command == 'help':
            print_usage()
        
        elif command == 'add':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            manager.add_task(title, description, due_date)
            print("Task added successfully!")
        
        elif command == 'list':
            tasks = manager.get_all_tasks()
            if not tasks:
                print("No tasks found.")
            else:
                print("\nCurrent Tasks:")
                for i, task in enumerate(tasks, 1):
                    status = "✓" if task.completed else " "
                    print(f"{i}. [{status}] {task.title} (Due: {task.due_date})")
                    print(f"   Description: {task.description}\n")
        
        elif command == 'complete':
            try:
                task_id = int(input("Enter task number to mark as complete: ")) - 1
                manager.complete_task(task_id)
                print("Task marked as complete!")
            except (ValueError, IndexError):
                print("Invalid task number!")
        
        elif command == 'delete':
            try:
                task_id = int(input("Enter task number to delete: ")) - 1
                manager.delete_task(task_id)
                print("Task deleted successfully!")
            except (ValueError, IndexError):
                print("Invalid task number!")
        
        elif command == 'quit':
            print("Goodbye!")
            sys.exit(0)
        
        else:
            print("Unknown command. Type 'help' for usage.")

if __name__ == '__main__':
    main()