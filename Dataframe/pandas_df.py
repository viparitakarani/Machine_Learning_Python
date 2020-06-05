#!/usr/local/anaconda3/bin/python

#https://pandas.pydata.org/pandas-docs/stable/10min.html
#playing with pandas data frame. 

import pandas as pd
import numpy as np

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


#create data range with date as the index(key) for 6 row
#and then fill the data frame/Matrix with the date index and put ABCD as the columns and random data
dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))


#print the data with index and columns name
print('\n\nDATA FRAME (df):')
print(df)


#print the data only
print('df.values :')
print(df.values)

#print first 2 records with the rows index and columns name
print('df.head(2) :')
print(df.head(2))

#transposing the matrix in data frame (rows as columns and columns to rows)
print('df.T :(transposing data') 
print(df.T)


#sort all matrix base on columns B
print("df.sort_values(by='B')")
print(df.sort_values(by='B'))

print("df.sort_values(by='B', ascending=False)")
print(df.sort_values(by='B', ascending=False))


#print 3 records of the matrix start with row no 0 
print('df[0:3]')
print(df[0:3])

#print  record with index '20130102' to '20130104'
print("df['20130102':'20130104']")
print(df['20130102':'20130104'])



#print matrix with its all index for columns A and B only
print("df.loc[:,['A','B']]")
print(df.loc[:,['A','B']])

#print matrix with index from '20130102' to '20130104' for columns A and B only
print("df.loc['20130102':'20130104',['A','B']]")
print(df.loc['20130102':'20130104',['A','B']])


#print data frame to csv file
print("PRINT DATA FRAME TO CSV")
df.to_csv('foo.csv')

#read data frame from csv and print all data inside of it
print("READ DATA FRAME FROM CSV")
df3=pd.read_csv('foo.csv')
print(df3)

#formating data frame with variative  data for each columns 
df2 = pd.DataFrame({ 'A' : 1.,
'B' : pd.Timestamp('20130102'),
'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
'D' : np.array([3] * 4,dtype='int32'),
'E' : pd.Categorical(["test","train","test","train"]),
'F' : 'foo' })



print('\n\nDATA FRAME 2 (df2)')
print(df2)

#print the data type for each of the ata frame columns 
print('df2,dtypes :')
print(df2.dtypes)

#print the data from column A of the data frame
print('df2.A :')
print(df2.A)

#print the last 2 record of the data frame
print('df2 tail(2) :')
print(df2.tail(2))

#print transposing the  data frame
print('df2.T :(transposing data')
print(df2.T)

