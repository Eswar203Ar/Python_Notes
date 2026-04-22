
def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    print(f"{n} factorial is {fact}")
    return
factorial(5)
factorial(7)
factorial(9)
    