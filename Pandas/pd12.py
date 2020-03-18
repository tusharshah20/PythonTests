import pandas as pd
import numpy as np

#Panel data
#pandas has a Panel data structure ie 3d interms or DF
#To create a Panel, you can use a dict of DataFrame objects or a three-dimensional ndarray
from pandas.io import data, wb
#or
from pandas_datareader import data, wb
#import pandas.io.data as web


pdata = pd.Panel(dict((stk, wb.get_data_yahoo(stk, '1/1/2009', '6/1/2012'))
for stk in ['AAPL', 'GOOG', 'MSFT', 'DELL']))

pdata

pdata = pdata.swapaxes('items', 'minor')
pdata['Adj Close']
#we can select all data at a particular date or a range of dates

pdata.ix[:, '6/1/2012', :]
pdata.ix['Adj Close', '5/22/2012':, :]

#An alternate way to represent panel data, especially for fitting statistical models, is in
#“stacked” DataFrame form:
stacked = pdata.ix[:, '5/30/2012':, :].to_frame()
stacked

#DataFrame has a related to_panel method, the inverse of to_frame:
stacked.to_panel()

