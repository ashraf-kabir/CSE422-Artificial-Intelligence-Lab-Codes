# -*- coding: utf-8 -*-
"""
Created on Wed May 15 22:49:22 2019

@author: ASUS
"""

#6. Print average of all numbers divisible by 3 and less than 100.

c = 0
avg = 0
sum = 0
for n in range(1, 100):
    if n % 3 == 0:
        print(str(n) + " ", end = "")
        c += 1
        sum += n
avg = sum/c
average = str(round(avg, 2))
print('\nAverage is {}'.format(average))
