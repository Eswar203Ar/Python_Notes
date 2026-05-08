#given nums (must be sorted)
nums = [10, 20, 60, 40, 50, 30]
key = int(input("Enter element to search: "))

# Binary search
def binary_search(nums, key):
        low = 0
        high = len(nums)-1

        while low<=high:
            mid = (low+high)//2

            if key == nums[mid]:
                print("Element found")
                return
            elif key < nums[mid]:
                high = mid-1
            elif(key>nums[mid]):
                low = mid+1
            else:
              print("Element not found")
            
binary_search(nums, key)