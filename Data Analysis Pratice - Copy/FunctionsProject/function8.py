## prime number by using function
def is_prime(n):
    count = 0
    for i in range(1,n+1):
        if(n%i==0):
            count+=1
    if(count==2):
        print("Prime number")
    else:
        print("Not prime number")
    return
is_prime(4)
is_prime(11)
is_prime(15)