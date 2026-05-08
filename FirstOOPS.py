## Normal Fucntion
"""
a = 10
def fun():
    print(f"value of fun {a}")
    return
fun()
    """
    
'''    
### By using OOPS concept 
class Test:
    a = 10
    def fun():
        print("fun")
        return
print(f" fun value {Test.a}")
Test.fun()
'''

## OOPS concept inside the 2 class 
class First:
    a = 10
    def fun():
        print("first")
        return
class second:
    a = 20
    def fun():
        print("Second")
        return
print(f"First fun : {First.a}")
print(f"second fun : {second.a}")
First.fun()
second.fun()