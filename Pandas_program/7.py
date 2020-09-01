import pandas as pd
import numpy as np
import matplotlib
df = pd.DataFrame(np.random.rand(10,4),columns=['a','b','c','d'])
df.plot.bar()
df.show()
