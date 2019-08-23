# -*- coding: utf-8 -*-
"""
Created on Wed May 15 22:59:33 2019

@author: ASUS
"""

#8. A list has 6 numbers. Print sum of the smallest and largest number, 
#sum of second smallest and second largest, and sum of third smallest and third largest number.

my_list = [2, 7, 5, 6, 8, 1]
print(my_list)
length = len(my_list)
my_list.sort()
print('\n')
# smallest and largest
largest = my_list[length-1]
smallest = my_list[0]
print("Largest number is {}".format(largest))
print("Smallest number is {}".format(smallest))
sum = largest + smallest
print('Sum of smallest and largest number {}'.format(sum))
print('\n')
# second smallest and second largest
secondLargest = my_list[length-2]
secondSmallest = my_list[1]
print("Second Largest number is {}".format(secondLargest))
print("Second Smallest number is {}".format(secondSmallest))
sumofSecondLnS = secondLargest + secondSmallest
print('Sum of second smallest and second largest number {}'.format(sumofSecondLnS))
print('\n')
# third smallest and third largest
thirdLargest = my_list[length-3]
thirdSmallest = my_list[2]
print("Third Largest number is {}".format(thirdLargest))
print("Third Smallest number is {}".format(thirdSmallest))
sumofThirdLnS = thirdLargest + thirdSmallest
print('Sum of third smallest and third largest number {}'.format(sumofThirdLnS))
