# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 09:21:02 2019

@author: 16301034
"""

import pandas as pd

from pandas import read_csv
from sklearn import tree

data = read_csv("data1.csv")


Taste = pd.Series([])

for i in range(len(data)):
    if data["Brand"][i] == "Snickers": 
        Taste[i]="Bitter"
  
    elif data["Brand"][i] == "Kit Kat": 
        Taste[i]="Sweet"
    
data.insert(3, "Taste", Taste) 

print(data.head())


data['Color'] = data['Color'].map({'Red': 0, 'Blue': 1})
data['Brand'] = data['Brand'].map({'Snickers': 0, 'Kit Kat': 1})
data['Taste'] = data['Taste'].map({'Bitter': 0, 'Sweet': 1})

predictors = ['Color', 'Brand', 'Taste']

X = data[predictors]
Y = data.Class

decisionTreeClassifier = tree.DecisionTreeClassifier(criterion="entropy")

dTree = decisionTreeClassifier.fit(X, Y)

dotData = tree.export_graphviz(dTree, out_file=None)

print(dotData)
