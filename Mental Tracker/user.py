# For user 

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.daily_entries = []

    def add_entry(self, entry):
        self.daily_entries.append(entry)

