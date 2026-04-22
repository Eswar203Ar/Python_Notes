## By using with return perfect number
def perfect(n):
    sum = 0
    for i in range(1,n):
        if(n%i==0):
            sum = sum + i
    if(n==sum):
        return "Perfect number"
    else:
        return "Not perfect number"
res = perfect(7)
print(res)