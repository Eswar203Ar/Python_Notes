## print Factors of 6 or (Divisible)
n = int(input("Enter Factors : "))
for i in range(1,n+1):
    
    if(n%i==0):
        print(i)