## count digits in the given string

m = "DataTeach@123$" 
count = 0
for ch in m:
     if(ch.isdigit()):
         count = count + 1
print(count)