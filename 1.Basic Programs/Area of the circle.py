# -*- coding: utf-8 -*-
"""
Created on Sat May 15 08:05:20 2021

@author: Aripandi
"""

def Area(r):
    PI = 3.14
    return PI*(r*r)


value = int(input("Enter the Area: "))
print("Area of the circle: ",Area(value))