## prime number by using with return function
def is_prime(n):
    count = 0
    for i in range(1,n+1):
        if(n%i==0):
            count = count + 1
    if(count==2):
        return "Prime number"
    else:
        return "Not primr number"
res = is_prime(5)
print(res)