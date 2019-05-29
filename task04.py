# -*- coding: utf-8 -*-
"""
Created on Wed May 15 10:12:42 2019

@author: 16301034
"""

#4. A copy center charges 50 won per copy for the first 100 copies and 30 won per copy for each additional copy. 
# Write a program that requests the number as input and displays the total cost.

x = int(input('Enter number: '))

if x <= 100:
    cost = x * 50
    print(cost)
else:
    cost = ((x * 50) - 50) +30
    print(cost)
    