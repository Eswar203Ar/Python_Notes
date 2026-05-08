try :
    a = int(input("Enter first num :"))
    b = int(input("Enter second num :"))
    c = a/b
    print(f"Quoficent = {c}")
except ValueError:
    print("Exception : Invalid Input")
except ZeroDivisionError:
    print("Exception : can't divide by 0")