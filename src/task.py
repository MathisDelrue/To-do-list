from dataclasses import dataclass
from datetime import datetime

@dataclass
class Task:
    title: str
    description: str
    due_date: str
    completed: bool = False

    def __post_init__(self):
        # Validate the due date format
        try:
            datetime.strptime(self.due_date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Due date must be in YYYY-MM-DD format")

    def mark_complete(self):
        self.completed = True

    def to_dict(self):
        return {
            'title': self.title,
            'description': self.description,
            'due_date': self.due_date,
            'completed': self.completed
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            title=data['title'],
            description=data['description'],
            due_date=data['due_date'],
            completed=data['completed']
        )