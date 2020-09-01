import numpy as np
import pandas as pd
data = pd.read_csv('pandas_tutorial_read.csv',delimiter=';')
print(data)
data1 = pd.read_csv('pandas_tutorial_read.csv', delimiter=';', names = ['my_datetime', 'event', 'country', 'user_id', 'source', 'topic'])
print(data1)
print(data1.head())
print(data1.tail())
