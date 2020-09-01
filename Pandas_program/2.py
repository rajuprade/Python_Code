import numpy as np
import pandas as pd
data=pd.read_csv('zoo.csv',delimiter=',')
print(data)
print(data.count())
print(data.water_need.sum())
print(data.water_need.min())
print(data.water_need.max())
print(data.water_need.mean())
print(data.water_need.median())
print(data.groupby('animal').mean())
zoo_eats = pd.DataFrame([['elephant','vegetables'], ['tiger','meat'], ['kangaroo','vegetables'], ['zebra','vegetables'], ['giraffe','vegetables']], columns=['animal', 'food'])
print(zoo_eats)
d=data.merge(zoo_eats)
print(d)
print('===================================================')
d1=data.merge(zoo_eats,how='outer')
print(d1)
d2=data.merge(zoo_eats,how='inner')
print(d2)
d3= data.sort_values('water_need')
print(d3)





