
"""
words = ["python","Java","react","andriod","css"]
s = [word[::-1] for word in words]
print(s)
"""
"""
words = ["python","Java","react","andriod","css"]
print([s[::-1] for s in words[::-1]])
"""
"""
words = ["python","Java","react","andriod","css"]
for i in range(len(words)-1,-1,-1):
    print(words[i][::-1])
"""
words = ["python","Java","react","andriod","css"]
for s in words[::-1]:
    print(s[::-1])