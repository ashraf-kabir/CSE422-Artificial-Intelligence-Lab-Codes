# -*- coding: utf-8 -*-
"""
Created on Tue May 28 18:20:56 2019

@author: ASUS
"""

import numpy as np

num1 = np.zeros(10)
num2 = np.ones(10)
num1 = np.reshape(num1,(5,2))
num2 = np.reshape(num2,(5,2))
concat_num = np.concatenate([num1,num2])
print(concat_num)