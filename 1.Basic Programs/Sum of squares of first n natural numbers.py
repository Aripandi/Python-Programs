# -*- coding: utf-8 -*-
"""
Created on Sun May 16 06:46:21 2021

@author: Aripandi
"""

n = int(input('Enter the Number: '))
add = 0

while(n>0):
    s = n**2
    add += s
    n-=1
    
print('Sum of Squares: ',add) 