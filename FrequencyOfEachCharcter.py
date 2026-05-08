## Frequency of each charcter in string using dictonary
s = 'datateachtraning'
freq = { }
for ch in s:
    if ch in freq :
        freq[ch] += 1
    else :
        freq[ch] = 1
print(freq)
        
    