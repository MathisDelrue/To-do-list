import json
import os
from task import Task

class TaskManager:
    def __init__(self, data_file='data/tasks.json'):
        self.data_file = data_file
        self.tasks = []
        self._load_tasks()

    def _ensure_data_dir(self):
        os.makedirs(os.path.dirname(self.data_file), exist_ok=True)

    def _load_tasks(self):
        self._ensure_data_dir()
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    data = json.load(f)
                    self.tasks = [Task.from_dict(task_data) for task_data in data]
            except (json.JSONDecodeError, FileNotFoundError):
                self.tasks = []

    def _save_tasks(self):
        self._ensure_data_dir()
        with open(self.data_file, 'w') as f:
            json.dump([task.to_dict() for task in self.tasks], f, indent=4)

    def add_task(self, title, description, due_date):
        task = Task(title, description, due_date)
        self.tasks.append(task)
        self._save_tasks()

    def get_all_tasks(self):
        return self.tasks

    def complete_task(self, task_id):
        if 0 <= task_id < len(self.tasks):
            self.tasks[task_id].mark_complete()
            self._save_tasks()
        else:
            raise IndexError("Task index out of range")

    def delete_task(self, task_id):
        if 0 <= task_id < len(self.tasks):
            del self.tasks[task_id]
            self._save_tasks()
        else:
            raise IndexError("Task index out of range")