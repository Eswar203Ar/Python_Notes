
nums = [1,2,3,4,5,6,7,8]
try:
    loc = int(input("Enter loc : "))
    print("Element is :", nums[loc])
except ValueError:
    print("Exception : loc must be int")
except IndexError:
    print("Exception : Index out of bound")