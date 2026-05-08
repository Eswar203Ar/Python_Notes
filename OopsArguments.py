## No arguments - no return value
'''
class say:
    def fun():
        print("Hi Hello")
        return
say.fun()
'''

## with args - No retun value
'''
class Do:
    def add(a,b):
        print(f"sum = {a+b}")
        return
    def sub(a,b):
        print(f"dif = {a-b}")
Do.add(10,20)
Do.sub(40,25)
'''
## With args - with return value
class check:
    def is_even(n):
        if n%2==0:
            return "Even"
        else:
            return "Not Even"
msg = check.is_even(10)
print(msg)