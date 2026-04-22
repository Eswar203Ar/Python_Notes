## Nested if --> writing if block inside another block
n = int(input("Enter n value :"))
if(n>0):
    if(n%2==0):
        print("Even number")
    else:
        print("Not even number")
else:
    print(f"Error : Negative number given")