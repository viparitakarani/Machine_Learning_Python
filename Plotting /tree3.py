#!/usr/local/anaconda3/bin/python


from __future__ import division

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.dict_vectorizer import DictVectorizer
from sklearn.linear_model.logistic import LogisticRegression
from sklearn.metrics.classification import classification_report, accuracy_score
from sklearn.naive_bayes import GaussianNB
from sklearn.tree.tree import DecisionTreeClassifier 

from sklearn import tree


import numpy as np
import pandas as pd


# Read the data into a pandas dataframe
df = pd.read_csv('adult.csv')

# Columns names
cols = np.array(['age', 'workclass', 'fnlwgt', 'education', 'education-num',
                 'marital-status', 'occupation', 'relationship', 'race', 'sex',
                 'capital-gain', 'capital-loss', 'hours-per-week', 'native-country',
                 'target'])

# numeric columns
numeric_cols = ['age', 'fnlwgt', 'education-num',
                'capital-gain', 'capital-loss', 'hours-per-week']

# assign names to the columns in the dataframe
df.columns = cols

# replace the target variable to 0 and 1 for <50K and >50k
df1 = df.copy()
df1.loc[df1['target'] == ' <=50K', 'target'] = 0
df1.loc[df1['target'] == ' >50K', 'target'] = 1

# split the data into train and test
X_train, X_test, y_train, y_test = train_test_split(
    df1.drop('target', axis=1), df1['target'], test_size=0.2)


# numeric attributes

x_num_train = X_train[numeric_cols].as_matrix()
x_num_test = X_test[numeric_cols].as_matrix()

# scale to <0,1>

max_train = np.amax(x_num_train, 0)
max_test = np.amax(x_num_test, 0)        # not really needed

x_num_train = x_num_train / max_train
x_num_test = x_num_test / max_train        # scale test by max_train

# labels or target attribute

y_train = y_train.astype(int)
y_test = y_test.astype(int)

# categorical attributes

cat_train = X_train.drop(numeric_cols, axis=1)
cat_test = X_test.drop(numeric_cols, axis=1)

cat_train.fillna('NA', inplace=True)
cat_test.fillna('NA', inplace=True)

x_cat_train = cat_train.T.to_dict().values()
x_cat_test = cat_test.T.to_dict().values()

# vectorize (encode as one hot)

vectorizer = DictVectorizer(sparse=False)
vec_x_cat_train = vectorizer.fit_transform(x_cat_train)
vec_x_cat_test = vectorizer.transform(x_cat_test)

# build the feature vector

x_train = np.hstack((x_num_train, vec_x_cat_train))
x_test = np.hstack((x_num_test, vec_x_cat_test))


#clfLR = LogisticRegression().fit(x_train, y_train.values)
#pred = clfLR.predict(x_test)
#print classification_report(y_test.values, pred, digits=4)
#print accuracy_score(y_test.values, pred)

clfTree = tree.DecisionTreeClassifier().fit(x_train, y_train)
predict = clfTree.predict(x_test)
#print classification_report(y_test.values, pred, digits=4)
#print accuracy_score(y_test.values, pred)

clfGNB = GaussianNB().fit(x_train, y_train)
predict = clfGNB.predict(x_test)
#print classification_report(y_test.values, pred, digits=4)
#print accuracy_score(y_test.values, pred)



#with open("adult.csv", 'w') as f:  
#    f = tree.export_graphviz(clf2, out_file=f)  

#import os  
#os.unlink('adult.csv')  



#Export to pdf
import pydotplus  
dot_data = tree.export_graphviz(clfTree, out_file=None)  
graph2 = pydotplus.graph_from_dot_data(dot_data)  
graph2.write_pdf("adulttree.pdf")  



dot_data = tree.export_graphviz(clfGNB, out_file=None)  
graph2 = pydotplus.graph_from_dot_data(dot_data)  
graph2.write_pdf("adulttree.pdf")  


#from IPython.display import Image  
#dot_data = tree.export_graphviz(clf2, out_file=None)  
#graph2 = pydotplus.graph_from_dot_data(dot_data)

## Color of nodes
#odes = graph2.get_node_list()

#for node in nodes:
#    if node.get_label():
#        values = [int(ii) for ii in node.get_label().split('value = [')[1].split(']')[0].split(',')];
#        color = {0: [255,255,224], 1: [255,224,255], 2: [224,255,255],}
#        values = color[values.index(max(values))]; # print(values)
#        color = '#{:02x}{:02x}{:02x}'.format(values[0], values[1], values[2]); # print(color)
#        node.set_fillcolor(color )
#

#Image(graph2.create_png() ) 
