## Import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
## Define path data
COLUMNS = ['age','workclass', 'fnlwgt', 'education', 'education_num', 'marital',
           'occupation', 'relationship', 'race', 'sex', 'capital_gain', 'capital_loss',
           'hours_week', 'native_country', 'label']
PATH ="adult.data"
df_train = pd.read_csv(PATH,skipinitialspace=True,names = COLUMNS,index_col=False)
print(df_train.shape)
print(df_train.groupby(['label']).mean())
df_plot = df_train.groupby(['label', 'marital'])['capital_gain'].mean().unstack()
plt.show(df_plot)
