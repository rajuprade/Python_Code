import numpy as np
import pandas as pd

data = pd.read_csv("adult.data",names=['a','b','c','d','e','f','g','h','i','g','k','l','m','n','o'])
#data2=data[['a','b']]
        
print(data.loc[:,['a','c']])
