### Try and except block
try :
    a = int(input("Enter first num :"))
    b = int(input("Enter second num  :"))
    c = a+b
    print(f"sum = {c}")
except ValueError:
    print("Exception : Inavalid Input")