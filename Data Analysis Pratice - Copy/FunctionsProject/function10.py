## Perfect number by using function
def is_perfect(n):
    sum = 0
    for i in range(1,n):
        if(n%i==0):
            sum = sum + i
    if(n==sum):
        print("Perfect number")
    else:
        print("Not perfect number")
    return
is_perfect(6)
is_perfect(8)
is_perfect(10)
is_perfect(12)