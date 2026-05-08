#Function Programming
'''
a = 20
def fun():
    print("Fun..")
    return
print(f"fun val : {a}")
fun()
'''

## Object Orineted programming EXample
'''
class Test:
    a = 10
    def fun():
        print("Fun - test")
        return
print(f"fun val : {Test.a}")
Test.fun()

'''

## Two class
class First :
    a = 10
    def fun():
        print("First - fun")
        return
class second:
    a = 20
    def fun():
        print("Second - fun")
        return
print(f"First fun val : {First.a}")
print(f"Second fun val : {second.a}")
First.fun()
second.fun()