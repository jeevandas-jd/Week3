import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import numpy as np
def plotter(dataFrame):
    pass

def analyzer(dataFrame):
    """
    This function takes a DataFrame as input and returns a dictionary with the following keys:
    - 'mean': The mean of the 'value' column
    - 'median': The median of the 'value' column
    - 'std': The standard deviation of the 'value' column
    """
    mean = dataFrame['value'].mean()
    median = dataFrame['value'].median()
    std = dataFrame['value'].std()

    return {
        'mean': mean,
        'median': median,
        'std': std
    }