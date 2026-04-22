## Factorial of 5
fact = 1
n = int(input("Enter n value :"))
for i in range(1, n+1):
    fact = fact * i
print(f"Factorial of {n} is : {fact}")