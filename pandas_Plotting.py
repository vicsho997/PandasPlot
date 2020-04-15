import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.close('all')

ts = pd.Series(np.random.randn(1000),
              index=pd.date_range('1/1/2000', periods=1000)) 
ts = ts.cumsum()

print(ts.plot())

#On a DataFrame, the plot() method is a convenience to plot all of the columns with labels:
df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index,
                  columns=['A', 'B', 'C', 'D'])

df = df.cumsum()

plt.figure()

df.plot()

plt.legend(loc='best')