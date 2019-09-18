# -*- coding: utf-8 -*-
"""
Created on Thu May 16 21:19:28 2019

@author: ASUS
"""

#7. A person born in 1980 can claim, "I will be x years old in the year x squared." '. What is the value of x?
#Hints: It forms a quadratic equation X^2-X-1980=0

x = 1
while (x*x != 1980 + x):
    x += 1
print('Value of x is {}'.format(x))
