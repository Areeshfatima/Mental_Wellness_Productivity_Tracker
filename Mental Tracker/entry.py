# For entries
from datetime import datetime

class Entry:
    def __init__(self, mood, stress_level, tasks_completed):
        self.date = datetime.now().strftime("%d-%m-%Y")
        self.mood = mood
        self.stress_level = stress_level
        self.tasks_completed = tasks_completed

