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


#Getting Data I/O
#Writing to a csv file
df.to_csv('foo23.csv')
#Reading from a csv file
print(pd.read_csv('foo23.csv'))

#Reading and Writing to HDF5
#Wrinting to a HDF5
df.to_hdf('foo.h5', 'df')
#Reading from a HDF5 Store
pd.read_hdf('foo.h5', 'df')

#Reading and writing to MS Excel
#Writing to an excel file
df.to_excel('foo23.xlsx', sheet_name='Sheet1')
#Reading from an excel file
pd.read_excel('foo23.xlsx', 'Sheet1', index_col=None, na_values=['NA'])