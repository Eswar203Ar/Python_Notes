

""" Display string charcter by charcter
for ch in s:
    print(ch)
    
    """
'''   
## Display only Alphabets in string:
for ch in s:
    if(ch.isalpha()):
        print(ch)
 '''
 

 ##count digits in the given string

s = "DataTeach@123$"
sum = 0
for ch in s :
    if(ch.isdigit()):
        sum = sum + int(ch)
print(sum) 
