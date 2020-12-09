import pandas as pd 
def load_csv(file, labels):
    return pd.read_csv(file)[labels]

