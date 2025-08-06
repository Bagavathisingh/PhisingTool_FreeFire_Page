import matplotlib as mp
import numpy as np
import pandas as pd

file = pd.read_csv('captured.csv')

file2 = file.head()

print(file2)