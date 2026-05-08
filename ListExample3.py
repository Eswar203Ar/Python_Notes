s = 'a3b2c4d3'
'''
for i in range(0,len(s) , 2):
    ch1 = s[i]
    ch2 = int(s[i+1])
    for j in range(ch2):
        print(ch1 , end = "")
        
 '''

result = " "
for i in range(0,len(s),2):
    ch = s[i]
    count = int(s[i+1])
    result += ch * count
print(result)
    
     
