import pandas as pd
import numpy as np
import os

os.getcwd()

def display():
    desired_width = 320
    pd.set_option('display.width', desired_width)
    pd.set_option('display.max_rows', 100)
    pd.set_option('display.max_columns', 50)
    np.set_printoptions(linewidth=desired_width)
