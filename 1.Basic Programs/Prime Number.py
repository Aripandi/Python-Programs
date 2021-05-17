# -*- coding: utf-8 -*-
"""
Created on Sat May 15 14:44:36 2021

@author: Aripandi
"""

n = int(input('Enter the Number: '))
isPrime = True

if(n==0 or n==1):
    isPrime = False
else:
    if(n>1):
        for i in range(2,n):
            if(n%i==0):
                isPrime = False
                break
            
            

if(isPrime):
    print(n,' is prime Number!')
else:
    print(n,' is not a prime Number!')
   

            

        
            

