## Check the table 13  by using for loop in oops
'''
class check:
    def Table(n):
        for i in range(1,11):
            print(f"{n} * {i} = {n*i}")
        
check.Table(13)
'''

## Check the biggest of 3 numbers
'''
class check :
    def big(a,b,c):
        if(a>b and a>c):
            print("a is big")
        elif(b>c):
            print("b is big")
        else:
            print("c is big")
        return
check.big(10,25,5)
'''

## Check the given args is vowel or not
class check:
    def vowels(ch):
        if(ch =='a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
            print("The given args is vowel")
        else:
            print("Not vowel")
        return
    
check.vowels('x')
        