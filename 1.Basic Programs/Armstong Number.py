# -*- coding: utf-8 -*-
"""
Created on Sat May 15 07:59:20 2021

@author: Aripandi
"""

num = int(input("Enter the Number: "))

order = len(str(num))

temp = num
sum=0

while(temp>0):
    digits = temp%10
    sum += digits**order
    temp //=10
    
    
if(num == sum):
    print(num,' is Armstrong')
else:
    print(num,' is not Armstrong')
    