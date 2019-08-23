# -*- coding: utf-8 -*-
"""
Created on Mon May 27 22:34:36 2019

@author: ASUS
"""

import numpy as np

path = "E:/workspaces/CSE422-Lab/CSE422-Lab02/file.txt"
txt = np.genfromtxt(path, delimiter=",",dtype = None)
print(txt)