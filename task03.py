# -*- coding: utf-8 -*-
"""
Created on Wed May 15 09:55:33 2019

@author: 16301034
"""

#3.Write a program that asks the user to enter a whole number of inches and convert that length to feet and inches. See the following figure. The program should use both integer division and the modulus operator. 
#Examples: Enter number of Inches: 185
#185 inches if 15 feet and 5 inches

import math
inches = float(input('Enter inches: '))
feet = inches / 12
f = math.floor(feet)
remInches = inches % 12
rI = math.floor(remInches)

print('{} feet and {} inches'.format(f, rI))
