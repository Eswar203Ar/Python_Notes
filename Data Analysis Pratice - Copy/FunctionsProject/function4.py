## Print factorial by using functions
def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    print(f"{n} factorials is {fact}")
    return
factorial(5)
factorial(10)
factorial(15)
factorial(20)
factorial(25)