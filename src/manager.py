import json
import os
from task import Task

class TaskManager:
    def __init__(self, data_file='data/tasks.json'):
        self.data_file = data_file
        self.tasks = []
        self._load_tasks()

    def _ensure_data_dir(self):
        try:
            os.makedirs(os.path.dirname(self.data_file), exist_ok=True)
        except Exception as e:
            raise ValueError(f"Failed to create data directory: {str(e)}")

    def _load_tasks(self):
        self._ensure_data_dir()
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    data = json.load(f)
                    self.tasks = [Task.from_dict(task_data) for task_data in data]
            except json.JSONDecodeError:
                print("Error: Tasks file is corrupted. Starting with empty task list.")
                self.tasks = []
            except FileNotFoundError:
                print("Error: Tasks file not found. Starting with empty task list.")
                self.tasks = []
            except Exception as e:
                print(f"Error loading tasks: {str(e)}. Starting with empty task list.")
                self.tasks = []

    def _save_tasks(self):
        self._ensure_data_dir()
        try:
            with open(self.data_file, 'w') as f:
                json.dump([task.to_dict() for task in self.tasks], f, indent=4)
        except Exception as e:
            raise ValueError(f"Failed to save tasks: {str(e)}. Please check file permissions and disk space.")

    def add_task(self, title, description, due_date):
        try:
            if not title or title.strip() == "":
                raise ValueError("Please provide a non-empty title for the task")
            if not description or description.strip() == "":
                raise ValueError("Please provide a non-empty description for the task")
            if not due_date or due_date.strip() == "":
                raise ValueError("Please provide a due date for the task")

            task = Task(title, description, due_date)
            self.tasks.append(task)
            self._save_tasks()
        except ValueError as e:
            error_msg = str(e)
            if "Title" in error_msg:
                raise ValueError(f"Title error: {error_msg}")
            elif "Description" in error_msg:
                raise ValueError(f"Description error: {error_msg}")
            elif "Due date" in error_msg or "date" in error_msg:
                raise ValueError(f"Due date error: {error_msg}")
            else:
                raise ValueError(f"Error creating task: {error_msg}")

    def get_all_tasks(self):
        return self.tasks

    def complete_task(self, task_id):
        try:
            if not isinstance(task_id, int):
                raise ValueError("Task ID must be a number")
            if task_id < 0:
                raise ValueError("Task ID cannot be negative")
            if task_id >= len(self.tasks):
                raise ValueError(f"Task with ID {task_id + 1} does not exist")

            self.tasks[task_id].mark_complete()
            self._save_tasks()
        except ValueError as e:
            raise ValueError(f"Error completing task: {str(e)}")

    def delete_task(self, task_id):
        try:
            if not isinstance(task_id, int):
                raise ValueError("Task ID must be a number")
            if task_id < 0:
                raise ValueError("Task ID cannot be negative")
            if task_id >= len(self.tasks):
                raise ValueError(f"Task with ID {task_id + 1} does not exist")

            del self.tasks[task_id]
            self._save_tasks()
        except ValueError as e:
            raise ValueError(f"Error deleting task: {str(e)}")