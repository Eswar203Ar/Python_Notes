## Display largest length word in the list along with index value without using max
words = ["python","Java","react","andriod","css"]
large = words[0]
index = 0
for s in range(1,len(words)):
    if(len(words[s]) > len(large)):
        large = words[s]
        index = s
print(f"Largest : {large}")
print(f"Index : {index}")
        
