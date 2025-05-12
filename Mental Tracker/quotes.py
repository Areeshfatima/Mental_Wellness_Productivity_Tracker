# Quotes

import random

class Quotes:
    def __init__(self):
        self.quotes = [
            "Believe you can and you are halfway there.",
            "Keep pushing forward.",
            "Everday is a second chance.",
            "Your limitation, it's only your imagination."
        ]

    def get_random_quotes(self):
        return random.choice(self.quotes)
    