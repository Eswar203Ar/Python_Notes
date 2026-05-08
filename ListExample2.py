## Check wheather given list to find the first and 2nd largest numbres
nums = [3,5,2,7,6,4]
first = nums[0]
second = nums[0]

for i in range(1,len(nums)):
    if (nums[i] > first):
        second = first
        first = nums[i]
    elif(nums[i] > second and nums[i] != first) :
        second = nums[i]   
print(first)
print(second)