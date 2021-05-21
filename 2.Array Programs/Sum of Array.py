# -*- coding: utf-8 -*-
"""
Created on Sun May 16 06:58:32 2021

@author: Aripandi
"""

def sum_of_arr(arr):
    
    sum = 0
    
    #using for loop to get into array
    for i in arr:
        sum = sum+i
        
    return sum 


arr = [1,23,44,56,6]
ans = sum_of_arr(arr)
print('Sum of the array: ',ans)


#method - 2

arr = []
arr = [12,34,56,33]

ans = sum(arr)
print('Sum of the array: ',ans)  
