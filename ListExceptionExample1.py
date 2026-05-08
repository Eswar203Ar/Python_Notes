nums = [1,2,5,0,9,5,3]
try :
    loc1 = int(input("Enter loc1 :"))
    loc2 = int(input("Enter loc2 :"))
    a = nums[loc1]
    b = nums[loc2]
    c = a/b
    print(f"Quoficent = {c}")
except ValueError:
    print("Exception : loc must be int")
except IndexError:
    print("Exception : Index out of range")
except ZeroDivisionError:
    print("Exception : can't divide by zero")