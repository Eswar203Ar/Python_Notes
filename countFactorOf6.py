## count Factor(Divisble of 6) 6
count = 0
n = int(input("Enter n values : "))
for i in range(1,n+1):
    if(n%i==0):
        count+=1
print(count)