## print the factorial number 5
fact = 1
n = int(input("Enter Factorial number : "))
for i in range(1,n+1):
    fact = fact * i
print(f"Factorial of {n} number is : {fact}")