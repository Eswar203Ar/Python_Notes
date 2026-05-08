nums=[3,5,9,4,6,12,7,8,2,10]
for n in nums:
     count=0
     for i in range(1,n+1):
          if(n%i==0):
               count = count+1
     if (count==2):
          print(f"{n}is prime")