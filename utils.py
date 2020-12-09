import pandas as pd 
import numpy as np
import scipy.stats
def load_csv(file, labels):
    return pd.read_csv(file)[labels]

def coeff_correl(col1, col2):
    return np.corrcoef(col1, col2)