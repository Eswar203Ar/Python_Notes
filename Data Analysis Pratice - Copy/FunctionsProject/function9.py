## Biggest of 3 numbers by using function
def big(a,b,c):
    if(a>b and a>c):
        print("a is big")
    elif(b>c):
        print("b is big ")
    else:
        print("c is big")
    return
big(10,12,6)