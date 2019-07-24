# -*- coding: utf-8 -*-
"""
Created on Thu May 16 21:12:28 2019

@author: ASUS
"""

#5. A calendar year divisible by four is a leap year, with the exception of the years ending in 00 (that is, those divisible by 100) and not divisible by 400. For instance the years 1600 and 2000 are leap years, but 1700, 1800, and 1900 are not. 
#Write a program that requests a year as input and states whether it is a leap year. 
#parameters = "/?access_token=%s" % (access_token)

year = int(input("Enter year: "))

if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
    print('{} is a leap year'.format(year))
else:
    print('{} is not a leap year'.format(year))
