nums=[3,5,9,4,6,12,7,8,2,10]
large=nums[0]
x=0
for i in range (1,len(nums)):
    if(nums[i]>large):
        large =nums[i]
        x=i
small = nums[0]
y=0
for i in range (1,len(nums)):
    if(nums[i]<small):
        small =nums[i]
        y=i
temp=nums[x]
nums[x]=nums[y]
nums[y]=temp
print("after swap list is: ")
for ele in nums:
     print(ele)