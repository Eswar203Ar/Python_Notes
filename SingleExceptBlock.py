'''
Exception is aparent class to all Exception 
we can handle mutliple exception in a single Except block
Everyexception has pre
'''
try :
    a = int(input("Enter first value : "))
    b = int(input("Enter second value :"))
    c = a/b
    print(f"Quoficent = {c}")
except Exception as msg:
    print(f"Exception : {msg}")