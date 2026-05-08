nums = [3,5,7,6,4]
large = nums[0]
for i in range(1,len(nums)):
    if nums[i] > large:
        large = nums[i]
print(large)