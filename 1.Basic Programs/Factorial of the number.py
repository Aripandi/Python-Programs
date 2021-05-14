# -*- coding: utf-8 -*-
"""
Created on Thu May 13 10:15:55 2021

@author: Aripandi
"""
#Factorial of the number using recursion

def factorial(n):
    
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
    
num = 5

print("Factorial of the number is: ",factorial(num))

#Iterative

def factorial(n):
    
    if(n<0):
        print("Enter positive number")
    elif(n==0 or n==1):
        return 1
    else:
        fact = 1
        while(n>1):
           fact *= n
           n -= 1 
        return fact
    
num = 5
print("Factorial of the number is: ",factorial(num))

#using built-in function
import math

def fact(n):
    
    return (math.factorial(n))

num=7
print("Factorial of the number is: ",fact(num))

        
    