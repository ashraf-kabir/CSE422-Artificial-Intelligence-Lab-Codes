# -*- coding: utf-8 -*-
"""
Created on Wed May 15 09:50:27 2019

@author: 16301034
"""

#2. Question 3. Write a program to convert temperature from Centigrade (C’) to Fahrenheit (F’) 
#Far=1.8Cel+32

c = float(input('Enter Celsius: '))

f = (1.8 * c) + 32

print('Fahrenheit {}'.format(f))
