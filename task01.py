# -*- coding: utf-8 -*-
"""
Created on Wed May 15 09:22:49 2019

@author: 16301034
"""

#1.Write a program that convert percentage to decimal.
#Example: Enter percentage: 125% 
#Equivalent decimal: 1.25

percent = input('Enter percentage: ')
percentage = float(percent.strip('%'))
result = percentage/100
print('Equivalent decimal: {}'.format(result))
