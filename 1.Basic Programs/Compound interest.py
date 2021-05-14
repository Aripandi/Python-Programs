def compound_interest(p,t,r):
    #p-principle
    #t - time period
    #r - rate of interest
    #A - Amount
    #CI- compound interest
    A = p*(pow(1+r/100,t))
    CI = A-p
    
    return CI

value = compound_interest(1200,2,5.4)
print("Compound interest: ",value)
