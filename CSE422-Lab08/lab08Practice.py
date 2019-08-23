# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 09:18:41 2019

@author: 16301034
"""

from pandas import read_csv
from sklearn import tree

data = read_csv("data.csv")
print(data.head())


data['Color'] = data['Color'].map({'Red': 0, 'Blue': 1})
data['Brand'] = data['Brand'].map({'Snickers': 0, 'Kit Kat': 1})

predictors = ['Color', 'Brand']

X = data[predictors]
Y = data.Class

decisionTreeClassifier = tree.DecisionTreeClassifier(criterion="entropy")

dTree = decisionTreeClassifier.fit(X, Y)

dotData = tree.export_graphviz(dTree, out_file=None)

print(dotData)


# after runnning this file copy digigraph

print(dTree.predict([[1, 1]]))

print(dTree.predict([[0, 0]]))