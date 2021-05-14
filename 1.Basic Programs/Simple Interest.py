# -*- coding: utf-8 -*-
"""
Created on Thu May 13 10:34:30 2021

@author: Aripandi
"""

def simple_interest(p,t,r):
    
    print("The principle amount is: ",p)
    print("The time period is: ",t)
    print("The rate of interest: ",r)
    
    si = (p*t*r)/100
    return si

value = simple_interest(10000,5,5)
print("The simple interest: ",value)