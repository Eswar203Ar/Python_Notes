## Biggest of 3 numbers by using with return function
def big(a,b,c):
    if(a>b and a>c):
        return "a is big"
    elif(b>c):
        return "b is big"
    else:
        return "c is big"
res = big(10,25,5)
print(res)