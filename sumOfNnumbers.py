## sum of first N natural numbers
sum = 0
n = int(input("Enter n value : "))
for i in range(1,n+1):
    sum = sum + i
print(f"sum of {n} number is : {sum}")