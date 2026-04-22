a = int(input("Enter a value:"))
b = int(input("Enter b value:"))
c = int(input("Enter c value:"))
d = int(input("Enter d value:"))
if(a>b and a>c and a>d):
    print("a is big")
elif(b>c and b>d):
    print("b id big")
elif(c>d):
    print("c is big")
else:
    print("d is big")