# -*- coding: utf-8 -*-
"""
Created on Wed May 15 10:32:07 2019

@author: 16301034
"""

#10.  Write a python program to find area of a triangle. Inputs are the 3 sides of triangle. 

import math

x = float(input('Enter the value of first side of triangle: '))
y = float(input('Enter the value of second side of triangle: '))
z = float(input('Enter the value of third side of triangle: '))

s = ((x+y+z)/2)

area = math.sqrt(s*(s-x)*(s-y)*(s-z))

a = str(round(area, 2))

print('Area of the triangle is {}'.format(a))
