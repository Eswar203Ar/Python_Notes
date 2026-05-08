words = ["python","Java","react","andriod","css"]
first = 0
second = 0
for i in words:
    if(i>first):
        second = first
        first = i
    elif(i > second and i != first):
        second = i
print(f"First largest word : {first}")
print(f"second largest word : {second}")
        