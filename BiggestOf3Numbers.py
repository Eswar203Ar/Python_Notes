a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter Third number"))
if(a!=b !=c): ## nested if condition the numbers should not equal
    if(a>b and a>c):
        print("a is big")
    elif(b>c):
        print("b is big")
    else:
        print('c is big')
else:
    print(f"Error : Not unique numbres")