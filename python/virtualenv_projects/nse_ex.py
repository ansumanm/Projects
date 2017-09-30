#!/Users/ansuman/Github/Projects/python/virtualenv/bin/python
#

from nsepy import get_history
from datetime import date
# from matplotlib import pyplot as plt

data = get_history(symbol="SBIN", start=date(2015, 1, 1), end=date(2015, 1, 31))
# data[['VWAP', 'Turnover']].plot(secondary_y='Turnover')
print(data)
