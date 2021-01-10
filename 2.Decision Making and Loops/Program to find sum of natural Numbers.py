# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 07:40:27 2021

@author: Aripandi
"""

n = int(input('Enter the number: '))

if n<0:
    print('Enter the Positive Number: ')
else:
    sum = 0
    while(n>0):
        sum += n
        n -= 1
print(f'sum of the Number is {sum}')
