# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 08:49:18 2021

@author: Aripandi
"""

a = int(input('Enter A: '))
b = int(input('Enter B: '))

a = a+b
b = a-b
a = a-b

print('After Swapping: \n')
print('A: {}\nB: {}'.format(a,b))