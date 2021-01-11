# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 12:27:31 2021

@author: Aripandi
"""

#Python program to find area of triangle

#get the value of three side

a = float(input('Enter First side: '))
b = float(input('Enter secocd side: '))
c = float(input('Enter third side: '))

#calculate perimeter

s = (a+b+c)/2

#Find area

area = (s*(s-a)*(s-b)*(s-c))**0.5

print('Area of Triangle {0:.2f}'.format(area))