# -*- coding: utf-8 -*-
"""
Created on Sun May 26 15:38:19 2019

@author: ASUS
"""

#import numpy as np

#def factorial():
#    my_array = []
#    for i in range(5):
#        my_array.append(int(input("Enter number: ")))
#    my_array = np.array(my_array)
#    print(np.floor(my_array))
#    
#factorial()

def factorial(n):
    if(n <= 1):
        return 1
    else:
        return(n*factorial(n-1))
n = int(input("Enter number: "))

print(factorial(n))