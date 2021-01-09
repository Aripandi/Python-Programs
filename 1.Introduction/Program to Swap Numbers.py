# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 08:22:03 2021

@author: Aripandi
"""

n1 = int(input('Enter Number1: '))
n2 = int(input('Enter Number2: '))

temp = n1;
n1 = n2;
n2 = temp;

print('Number1: {}'.format(n1))
print('Number2: {}'.format(n2))