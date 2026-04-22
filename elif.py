## Elif is used for more than 2 conditions
## Shape of the triangle/Rectangle/pentagon/other
sides = int(input("Enter num of sides : "))
if(sides == 3):
    print("Triangle")
elif(sides == 4):
    print("Rectangle")
elif(sides == 5):
    print("Pentagon")
else:
    print("Other shapes")
