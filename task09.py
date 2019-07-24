# -*- coding: utf-8 -*-
"""
Created on Wed May 15 23:37:27 2019

@author: ASUS
"""

#9. Make a list with 10 numbers and print: (a) the difference between average number and smallest number, and 
# (b) difference between average and largest number.

my_list = [2, 7, 5, 6, 8, 2, 12, 15, 6, 3]
print(my_list)
length = len(my_list)
my_list.sort()
print('\n')

smallest = my_list[0]
largest = my_list[length-1]
print("Smallest number is {}".format(smallest))
print("Largest number is {}".format(largest))

avg = sum(my_list) / length
average = float(round(avg, 2))
print('Average is {}'.format(average))

diffOfAnS = abs(average - smallest)
print('difference between average number and smallest number is {}'.format(diffOfAnS))

diffOfAnL = abs(average - largest)
print('difference between average number and largest number is {}'.format(diffOfAnL))
