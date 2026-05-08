## perfect number 
sum = 0
n = int(input("Enter n value :"))
for i in range(1,n+1):
    if(n%i==0):
        sum = sum + i
if(n==sum):
    print("Perfect number")
else:
    print(" Not Perfect number")