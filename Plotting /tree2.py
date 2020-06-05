#!/usr/local/anaconda3/bin/python

import csv
import numpy as np
from os.path import dirname, exists, expanduser, isdir, join, splitext
from sklearn.datasets import load_iris  
from sklearn import tree  



def load_data(module_path, data_file_name):
    with open(join(module_path, '', data_file_name)) as csv_file:
        data_file = csv.reader(csv_file)
        temp = next(data_file)
        print (temp[1])
        n_samples = int(temp[0])
        n_features = int(temp[1])
        target_names = np.array(temp[2:])
        data = np.empty((n_samples, n_features))
        target = np.empty((n_samples,), dtype=np.int)

        for i, ir in enumerate(data_file):
            data[i] = np.asarray(ir[:-1], dtype=np.float64)
            target[i] = np.asarray(ir[-1], dtype=np.int)

    return data, target, target_names




clf2 = tree.DecisionTreeClassifier()  
data, target, target_names = load_data(dirname(__file__),'adult.csv')


clf2 = clf2.fit(data, target)  

with open("adult.csv", 'w') as f:  
    f = tree.export_graphviz(clf2, out_file=f)  

import os  
os.unlink('adult.csv')  

import pydotplus  
dot_data = tree.export_graphviz(clf2, out_file=None)  
graph2 = pydotplus.graph_from_dot_data(dot_data)  
graph2.write_pdf("iadult.pdf")  

from IPython.display import Image  
dot_data = tree.export_graphviz(clf2, out_file=None,  
                     feature_names=iris.feature_names,  
                     class_names=iris.target_names,  
                     filled=True, rounded=True,  # leaves_parallel=True, 
                     special_characters=True)  
graph2 = pydotplus.graph_from_dot_data(dot_data)

## Color of nodes
nodes = graph2.get_node_list()

for node in nodes:
    if node.get_label():
        values = [int(ii) for ii in node.get_label().split('value = [')[1].split(']')[0].split(',')];
        color = {0: [255,255,224], 1: [255,224,255], 2: [224,255,255],}
        values = color[values.index(max(values))]; # print(values)
        color = '#{:02x}{:02x}{:02x}'.format(values[0], values[1], values[2]); # print(color)
        node.set_fillcolor(color )
#

Image(graph2.create_png() ) 
