# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 09:20:29 2019

@author: 16301034
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

#import scikitplot as skplt

from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
#from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

from sklearn import metrics

from sklearn.metrics import roc_curve

from sklearn.metrics import roc_auc_score
#%matplotlib inline

dataset = pd.read_csv("/Users/Asus/Desktop/CSE422-Lab06/Social_Network_Ads.csv")
#dataset.head()

#X, y = load_iris(return_X_y=True)
#print(X)
#print(y)

gender = {'Male': 1,'Female': 0}

dataset.Gender = [gender[item] for item in dataset.Gender]

X = dataset[['Gender', 'Age', 'EstimatedSalary']]
y = dataset['Purchased']

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.4)

#
clf = LogisticRegression().fit(X_train, y_train)
ypred=clf.predict(X_test)
#
print(ypred)
yPro=clf.predict_proba(X_test) 
print(yPro)
sc=clf.score(X_test, y_test)
print(sc)
#
cm = confusion_matrix(y_test,ypred)
#
print(cm)

#skplt.metrics.plot_roc_curve(y, ypred)
#plt.show()




def plot_roc_curve(fpr, tpr):  
    plt.plot(fpr, tpr, color='orange', label='ROC')
    plt.plot([0, 1], [0, 1], color='darkblue', linestyle='--')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic (ROC) Curve')
    plt.legend()
    plt.show()


fpr, tpr, thresholds = roc_curve(y_test, ypred)
plot_roc_curve(fpr, tpr)






#ypred = clf.predict_proba(X_test)[::,1]
#fpr, tpr, _ = metrics.roc_curve(y_test,  ypred)
#auc = metrics.roc_auc_score(y_test, ypred)
#plt.plot(fpr,tpr,label="data 1, auc="+str(auc))
#plt.legend(loc=4)
#plt.show()







#probs = model.predict_proba(X_test)
#preds = probs[:,1]
#fpr, tpr, threshold = metrics.roc_curve(y_test, preds)
#roc_auc = metrics.auc(fpr, tpr)
#
## method I: plt
#
#plt.title('Receiver Operating Characteristic')
#plt.plot(fpr, tpr, 'b', label = 'AUC = %0.2f' % roc_auc)
#plt.legend(loc = 'lower right')
#plt.plot([0, 1], [0, 1],'r--')
#plt.xlim([0, 1])
#plt.ylim([0, 1])
#plt.ylabel('True Positive Rate')
#plt.xlabel('False Positive Rate')
#plt.show()