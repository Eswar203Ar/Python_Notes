## sum of the even numbers
sum = 0
for i in range(1,12):
    if(i%2==0):
        sum = sum + i
print(f"sum of even numbers : {sum}")