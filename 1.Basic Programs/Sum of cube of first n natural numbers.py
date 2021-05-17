# -*- coding: utf-8 -*-
"""
Created on Sun May 16 06:51:26 2021

@author: Aripandi
"""

n = int(input('Enter the Number: '))
add = 0

while(n>0):
    s = n**3
    add += s
    n-=1
    
print('Sum of Squares: ',add) 