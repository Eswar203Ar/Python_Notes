nums= [5, 10, 15, 20, 25]
ele = int(input("Enter the element to search: "))

for i in range(len(nums)):
    if nums[i] ==ele:
        print("Element found ")
        break
else:
    print("Element not found")