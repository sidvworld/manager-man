from datetime import datetime

class task:
    def __init__(self, task_name, task_deadline, task_priority):
        self.task_name = task_name
        self.task_deadline = task_deadline
        self.task_priority = task_priority
        self.created_at = datetime.now().strftime("%Y-%m-%d %I:%M %p")

test = task("test", "2023", "high")

print(test.task_name)
print(test.task_deadline)
print(test.task_priority)
print(test.created_at)