## prime number 
count = 0
n = int(input("Enter n values : "))
for i in range(1,n+1):
    if(n%i==0):
        count+=1
if(count == 2):
    print("Prime number")
else:
    print("Not prime number")