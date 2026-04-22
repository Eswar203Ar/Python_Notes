# count of factor
count = 0
n = int(input("Enterr n value :"))
for i in range(1, n+1):
    if(n%i == 0):
        count+=1
print(f"count of {n} is {count}")