num = [3,4,7,5,6,2,8]
first = 0
second = 0
for i in num:
    if(i > first):
        second = first
        first = i
    elif(i > second):
        second = i
print(f"First Largest : {first}")
print(f"Second largest : {second}")