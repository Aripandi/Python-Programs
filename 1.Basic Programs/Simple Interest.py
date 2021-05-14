def simple_interest(p,t,r):
    
    print("The principle amount is: ",p)
    print("The time period is: ",t)
    print("The rate of interest: ",r)
    
    si = (p*t*r)/100
    return si

value = simple_interest(10000,5,5)
print("The simple interest: ",value)
