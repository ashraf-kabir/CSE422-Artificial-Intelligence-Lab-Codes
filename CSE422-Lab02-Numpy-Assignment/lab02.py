# -*- coding: utf-8 -*-
"""
Created on Wed May 22 08:21:28 2019

@author: 16301034
"""

import numpy as np

# part0
#arr = np.array([[[1,2,3],[4,5,6]], [[7,8,9], [0,1,2]]])
#print(arr)

# part1
#x = np.arange(0,20,2)   # arrange(start,finish,step,dty)
#print(x[0:])   # 0 to last index
#print(x[0::2])   # 0 to lst index with 2 step
#print(x[0:7:2])    # 0 to 6 index with 2 step
#print(x[::-1])    # all in reverse

# part2
#np.random.seed(0)
#x1 = np.random.randint(10, size=6)
#print(x1)
#x2 = np.random.randint(10, size=(5,2))
#print(x2)
#x3 = np.random.randint(20, size=(5,2,2))
#print(x3)
#print(x3.ndim, x3.shape, x3.size)

# part3
mat = np.arange(0,20)
print(mat.shape)
mat = np.reshape(mat,(5,2,2))
print(mat)
print(mat.shape)

# part4
#zero_mat = np.zeros((5,4))
#zero_mat_alt = np.zeros(2)
#print(zero_mat_alt)   #has shape

# part5
#mat1 = np.array([4,5,6])
#mat2 = np.array([9,8,1])
#concat_mat = np.concatenate([mat1,mat2])
#print(concat_mat)

# part6
#mat1 = np.array([4,5,6,7,8,9])
#index_mat1 = np.where(mat1>7)
#print(index_mat1)

# part7
#path = "E:/workspaces/CSE422-Lab/CSE422-Lab02/iris.csv"
#iris = np.genfromtxt(path, delimiter=",",dtype = None)
#print(iris)