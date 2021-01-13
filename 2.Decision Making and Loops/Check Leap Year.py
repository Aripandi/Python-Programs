# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 19:53:23 2021

@author: Aripandi
"""

year = int(input('Enter the Year: '))

if(year%4==0):
    if(year%100==0):
        if(year%400==0):
            print('{0} is a leap Year'.format(year))
        else:
            print('{0} is not Leap Year'.format(year))
    else:
        print('{0} is leap year'.format(year))
else:
    print('{0} is not leap Year'.format(year))   