#!/usr/local/anaconda3/bin/python


from sklearn.datasets import load_iris  
from sklearn import tree  
iris = load_iris()  
clf2 = tree.DecisionTreeClassifier()  
clf2 = clf2.fit(iris.data, iris.target)  

with open("iris.csv", 'w') as f:  
    f = tree.export_graphviz(clf2, out_file=f)  

import os  
os.unlink('iris.csv')  

import pydotplus  
dot_data = tree.export_graphviz(clf2, out_file=None)  
graph2 = pydotplus.graph_from_dot_data(dot_data)  
graph2.write_pdf("iris.pdf")  

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
