# Tracker 

import pandas as pd  # powerful library using data handling of user
import matplotlib.pyplot as plt   # for graphs

class Tracker:
    def __init__(self, filename= "mood_log.csv"):
        self.filename = filename

    def save_entry(self, entry):
        df = pd.DataFrame([vars(entry)])
        df.to_csv(self.filename, mode= "a", header= not pd.io.common.file_exists(self.filename), index= False)

    def load_entries(self):
        try:
            return pd.read_csv(self.filename)
        except FileNotFoundError:
            return pd.DataFrame()

