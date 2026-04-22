## sum of factors by using function
def sum_factors(n):
    sum = 0
    for i in range(1,n):
        if(n%i==0):
            sum = sum + i
    print(f"sum of {n} factors is : {sum}")
    return
sum_factors(6)
sum_factors(8)
sum_factors(10)