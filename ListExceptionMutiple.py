nums = [1,3,5,7,9,2,4,6]
try :
    loc = int(input("Enter loc : "))
    print("Element :" , nums[loc])
except Exception as msg:
    print(f"Exception : {msg}")