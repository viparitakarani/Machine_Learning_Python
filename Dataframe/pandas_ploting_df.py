#!/usr/local/anaconda3/bin/python

#https://pandas.pydata.org/pandas-docs/stable/10min.html
#playing with pandas data frame. 


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


#create data range with date as the index(key) for 6 row
#and then fill the data frame/Matrix with the date index and put ABCD as the columns and random data
dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

#format the font
font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 16,
        }


#Ploting the data frame 
# Create a Figure
fig = plt.figure()

# Set up Axes
ax = fig.add_subplot(1,1,1)
ax.plot(df)
ax.text(0.5, 0.1, 
	r'$\cos(2 \pi t) \exp(-t)$',
        verticalalignment='bottom', 
	horizontalalignment='right',
        transform=ax.transAxes,
        color='green', 
	fontdict=font)

#plt.plot(df)
#plt.xlabel('Date')
#plt.ylabel('Random Number')
#plt.title('Histogram')
#plt.grid(True)
#plt.text(2,0.5, 'dataframe',fontsize=12, horizontalalignment='center',verticalalignment='center')
#plt.text(0.5,2,  r'$\cos(2 \pi t) \exp(-t)$' , fontdict=font)

plt.show()