## no args - no retrun values
'''
class say:
    def hello():
        print("Hi Hello Everyone")
        return
say.hello()
'''

## with args - no retrun values
'''
class Do:
    def add(a,b):
        print(f"sum is : {a+b}")
        return
    def sub(a,b):
        print(f"Diff is : {a-b}")
        return
Do.add(10,15)
Do.sub(20,5)    
'''

## With args - with retrun values
class check:
    def is_even(n):
        if n%2==0:
            return "Even"
        else:
            return "Not Even"
        
msg = check.is_even(8)
print(msg)