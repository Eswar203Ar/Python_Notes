## print factors of 6 by using function 
def factors(n):
    for i in range(1,n):
        if(n%i==0):
            print(f"factor {n} is {i}")
    return
factors(6)
factors(7)
factors(9)
factors(11)