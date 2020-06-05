#!/usr/local/anaconda3/bin/python

import pandas as pd
from scipy.spatial.distance import cosine
#pd.set_option('display.height', 1000)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)



# Create columns we are going to use
d_cols 	= ['user_id', 'item_id', 'rating']
# Read a file and select only 3 columns and the encoding help us to avoid error. Sep = seperated by
data 	= pd.read_csv('u.data', sep=',', names=d_cols, usecols=range(3), encoding='latin-1')


#berisi user_id dari 1-57 dan item_id dari 0-9 dan ratings

print("DATA FILE")
print(data)






print ("\n\n\nITEM-ITEM RECOMENDATION:")
#print(len(data.groupby("user_id"))) #==58 termasuk nama kolom
#m_cols = ['item_id', 'item']
#mapping = pd.read_csv('u.itemmapping', sep=',',usecols=range(2), encoding='latin-1')

#mapping= mapping.item_id.drop([0])
#items1= mapping.item.drop([0])

#ratings = pd.merge(mapping, data)

#print(len(ratings))
#print(ratings)

movieRatings = data.pivot_table(index=['user_id'],columns=['item_id'],values='rating',aggfunc=lambda x: len(x.unique()),fill_value=0)

#movieRatingsMapping = ratings.pivot_table(index=['user_id'],columns=['item'],values='rating',aggfunc=lambda x: len(x.unique()),fill_value=0)
#print movieRatingsMapping


#movieRatings.reset_index(inplace=True)
#movieRatings = movieRatings.drop('user_id', axis=1)
#movieRatings = movieRatings.drop('item_id', axis=1)

print("\nMATRIX Preference USER-ITEM-PREFERANCE")
print(movieRatings)


tmpMovieRatings = pd.DataFrame(index=movieRatings.columns,columns=movieRatings.columns)


#print(movieRatings.ix[0,:])
#print(1-cosine(movieRatings.ix[:,0],movieRatings.ix[:,1]))


#matix item x item yang masih kosong
print("\nMATRIX ITEM-ITEM yang masih kosong")
print (tmpMovieRatings)




#print(len(tmpMovieRatings.columns))


for i in range(0,len(tmpMovieRatings.columns)) :
    for j in range(0,len(tmpMovieRatings.columns)) :
        tmpMovieRatings.ix[i,j] = 1-cosine(movieRatings.ix[:,i],movieRatings.ix[:,j])


print ("\nCOMPLETE MATRIX SIMILARITY:")
tempMovieMapping=tmpMovieRatings.copy()
#tempMovieMapping.columns=items1
#tempMovieMapping.index=items1

print (tempMovieMapping)



#print (similar_movies)

print ("\n4 BEST  RECOMENDATION:")

#mapping = pd.read_csv('u.itemmapping', sep=',',usecols=range(2), encoding='latin-1')

#print(mapping.ix[0:5,1:2])
#similar_movies.columns=mapping.ix[0:,1:2]


#print tmpMovieRatings 
x=4
similar_movies = pd.DataFrame(index=tempMovieMapping.columns,columns=range(1,x+1))
for i in range(0,len(tempMovieMapping.columns)): 
    similar_movies.ix[i,:] = tempMovieMapping.ix[:,i].sort_values(ascending=False)[:x].index

print (similar_movies)





print ("\n\n\n\nUSER-USER RECOMENDATION:")

# Create columns we are going to use
d_cols = ['user_id', 'item_id', 'rating']
# Read a file and select only 3 columns and the encoding help us to avoid error. Sep = seperated by
data = pd.read_csv('u.data', sep=',', names=d_cols, usecols=range(3), encoding='latin-1')


#m_cols = ['user_id', 'user']
#mapping = pd.read_csv('u.usermapping', sep=',', names=m_cols, usecols=range(2), encoding='latin-1')

#mapping= mapping.user_id.drop([0])
#user1= mapping.user.drop([0])

#print(user1.to_string())

#ratings = pd.merge(mapping, data)
#print(ratings)

movieRatings = data.pivot_table(index=['user_id'],columns=['item_id'],values='rating',aggfunc=lambda x: len(x.unique()),fill_value=0)
#print (movieRatings)
#movieRatingsMapping = ratings.pivot_table(index=['user_id'],columns=['item'],values='rating',aggfunc=lambda x: len(x.unique()),fill_value=0)
#print movieRatingsMapping


#movieRatings.reset_index(inplace=True)
#movieRatings = movieRatings.drop('item_id', axis=1)
#movieRatings = movieRatings.drop('user_id', axis=1)

print("\nMATRIX Preference USER-ITEM-PREFERANCE")
print (movieRatings)

tmpMovieRatings = pd.DataFrame(index=movieRatings.index,columns=movieRatings.index)



print("\nMATRIX USER-USER yang masih kosong")

print (tmpMovieRatings)

for i in range(1,len(tmpMovieRatings.index)+1) :
    for j in range(1,len(tmpMovieRatings.index)+1) :
        tmpMovieRatings.ix[i,j] = 1-cosine(movieRatings.ix[i,:],movieRatings.ix[j,:])
        


print("\n")

print ("COMPLETE MATRIX SIMILARITY:")
tempMovieMapping=tmpMovieRatings.copy()
#tempMovieMapping.columns=user1
#tempMovieMapping.index=user1
print (tempMovieMapping)



print("\n")
print ("4 BEST  RECOMENDATION:")

x=4
similar_users = pd.DataFrame(index=tempMovieMapping.index,columns=range(1,x+1))

for i in range(1,len(tempMovieMapping.index)+1): 
    similar_users.ix[i,:] = tempMovieMapping.ix[i,:].sort_values(ascending=False)[:x].index

print(similar_users)


