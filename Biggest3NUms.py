##WAP to find biggest of 3 nums
a = int(input("Enter first num : "))
b = int(input("Enter second num : "))
c = int(input("Enter Third num : "))
if(a>b and a>c):
    print("a is big")
elif(b>c):
    print("b is big")
else:
    print("c is big")
