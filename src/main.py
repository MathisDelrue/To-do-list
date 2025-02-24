#!/usr/bin/env python3

import sys
import os
from task import Task
from manager import TaskManager
from colorama import init, Fore, Back, Style

# Initialize colorama for cross-platform colored output
init()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_usage():
    clear_screen()
    print(f"\n{Fore.CYAN}╔══════════════════════════════╗{Style.RESET_ALL}")
    print(f"{Fore.CYAN}║{Style.BRIGHT}      To-Do List Manager      {Style.RESET_ALL}{Fore.CYAN}║{Style.RESET_ALL}")
    print(f"{Fore.CYAN}╚══════════════════════════════╝{Style.RESET_ALL}\n")
    print(f"{Fore.YELLOW}Available Commands:{Style.RESET_ALL}")
    print(f"  {Fore.GREEN}1.{Style.RESET_ALL} add       - Add a new task")
    print(f"  {Fore.GREEN}2.{Style.RESET_ALL} list      - List all tasks")
    print(f"  {Fore.GREEN}3.{Style.RESET_ALL} complete  - Mark a task as complete")
    print(f"  {Fore.GREEN}4.{Style.RESET_ALL} delete    - Delete a task")
    print(f"  {Fore.GREEN}5.{Style.RESET_ALL} quit      - Exit the application\n")

def main():
    manager = TaskManager()
    print_usage()
    
    while True:
        command = input(f"{Fore.CYAN}┌──({Style.BRIGHT}Todo{Style.RESET_ALL}{Fore.CYAN})\n└─$ {Style.RESET_ALL}").strip().lower()
        
        if command in ['help', '?']:
            print_usage()
        
        elif command in ['add', '1']:
            clear_screen()
            print(f"{Fore.YELLOW}=== Add New Task ==={Style.RESET_ALL}\n")
            try:
                title = input(f"{Fore.GREEN}Enter task title:{Style.RESET_ALL} ")
                description = input(f"{Fore.GREEN}Enter task description:{Style.RESET_ALL} ")
                due_date = input(f"{Fore.GREEN}Enter due date (YYYY-MM-DD):{Style.RESET_ALL} ")
                manager.add_task(title, description, due_date)
                print(f"\n{Fore.GREEN}✓ Task added successfully!{Style.RESET_ALL}\n")
            except ValueError as e:
                print(f"\n{Fore.RED}✗ Error: {str(e)}{Style.RESET_ALL}\n")
        
        elif command in ['list', '2']:
            clear_screen()
            tasks = manager.get_all_tasks()
            if not tasks:
                print(f"\n{Fore.YELLOW}No tasks found.{Style.RESET_ALL}\n")
            else:
                print(f"\n{Fore.YELLOW}=== Current Tasks ==={Style.RESET_ALL}\n")
                # Print header
                print(f"{Fore.CYAN}{'ID':^4} {'Status':^8} {'Title':<20} {'Due Date':<12} {'Description':<30}{Style.RESET_ALL}")
                print(f"{Fore.CYAN}{'-'*74}{Style.RESET_ALL}")
                
                for i, task in enumerate(tasks, 1):
                    status = f"{Fore.GREEN}✓{Style.RESET_ALL}" if task.completed else f"{Fore.RED}✗{Style.RESET_ALL}"
                    print(f"{i:^4} {status:^8} {task.title:<20} {task.due_date:<12} {task.description:<30}")
                print()  # Add empty line after the list
        
        elif command in ['complete', '3']:
            try:
                task_id = int(input(f"\n{Fore.GREEN}Enter task number to mark as complete:{Style.RESET_ALL} ")) - 1
                manager.complete_task(task_id)
                print(f"\n{Fore.GREEN}✓ Task marked as complete!{Style.RESET_ALL}\n")
            except ValueError as e:
                print(f"\n{Fore.RED}✗ Error: {str(e)}{Style.RESET_ALL}\n")
        
        elif command in ['delete', '4']:
            try:
                task_id = int(input(f"\n{Fore.RED}Enter task number to delete:{Style.RESET_ALL} ")) - 1
                manager.delete_task(task_id)
                print(f"\n{Fore.GREEN}✓ Task deleted successfully!{Style.RESET_ALL}\n")
            except ValueError as e:
                print(f"\n{Fore.RED}✗ Error: {str(e)}{Style.RESET_ALL}\n")
        
        elif command in ['quit', '5', 'exit']:
            print(f"\n{Fore.YELLOW}Goodbye!{Style.RESET_ALL}\n")
            sys.exit(0)
        
        else:
            print(f"\n{Fore.RED}✗ Unknown command. Type 'help' or '?' for usage.{Style.RESET_ALL}\n")

if __name__ == '__main__':
    main()