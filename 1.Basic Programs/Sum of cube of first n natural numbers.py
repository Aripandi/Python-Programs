n = int(input('Enter the Number: '))
add = 0

while(n>0):
    s = n**3
    add += s
    n-=1
    
print('Sum of Squares: ',add) 
