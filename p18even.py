nums = [3,5,9,4,6,12,7,8,2,10]

for i in range(len(nums) - 1):
    if nums[i] % 2 == 0 and nums[i + 1] % 2 == 0:
        nums[i], nums[i + 1] = nums[i + 1], nums[i]

print(nums)