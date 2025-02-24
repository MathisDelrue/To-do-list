from dataclasses import dataclass
from datetime import datetime

@dataclass
class Task:
    title: str
    description: str
    due_date: str
    completed: bool = False

    def __post_init__(self):
        # Validate and sanitize title
        if not self.title:
            raise ValueError("Title is required")
        self.title = self.title.strip()
        if not self.title:
            raise ValueError("Title cannot be just whitespace")

        # Validate and sanitize description
        if not self.description:
            raise ValueError("Description is required")
        self.description = self.description.strip()
        if not self.description:
            raise ValueError("Description cannot be just whitespace")

        # Validate and sanitize due date
        if not self.due_date:
            raise ValueError("Due date is required")
        self.due_date = self.due_date.strip()
        if not self.due_date:
            raise ValueError("Due date cannot be just whitespace")

        # Validate the due date format and value
        try:
            date_parts = self.due_date.split('-')
            if len(date_parts) != 3:
                raise ValueError("Due date must be in YYYY-MM-DD format (e.g., 2026-12-31)")
            
            year, month, day = date_parts
            if not (year.isdigit() and month.isdigit() and day.isdigit()):
                raise ValueError("Year, month, and day must be numbers")
                
            date_obj = datetime.strptime(self.due_date, '%Y-%m-%d')
            
            # Validate reasonable year range
            current_year = datetime.now().year
            if not (current_year - 1 <= int(year) <= current_year + 10):
                raise ValueError(f"Year must be between {current_year - 1} and {current_year + 10}")
                
        except ValueError as e:
            if "unconverted data remains" in str(e) or "does not match format" in str(e):
                raise ValueError("Due date must be in YYYY-MM-DD format (e.g., 2023-12-31)")
            elif "out of range" in str(e):
                raise ValueError("Invalid date: Please check that month is 1-12 and day is valid for the given month")
            else:
                raise

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