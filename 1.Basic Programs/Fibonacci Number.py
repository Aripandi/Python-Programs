# -*- coding: utf-8 -*-
"""
Created on Sat May 15 08:22:52 2021

@author: Aripandi
"""

def fib(n):
    a = 0
    b = 1
    
    if n<0 or n==0:
        print('Invaild input!')
    elif n==1:
        return a
    elif n==2:
        return b
    else:
        for i in range(2,n):
            c = a+b
            a = b
            b = c
            
        return c
    
    
    
value = int(input("Enter the Number: "))
print(fib(value))



#using recursion
"""def fib(n):
    
    if n<0 or n==0:
        print("invalid Input")
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        
        return fib(n-1)+fib(n-2)
    
    
value = int(input("Enter the Number: "))
print(fib(value))"""