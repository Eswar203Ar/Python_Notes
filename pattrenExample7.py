## Display the # and $ symbols 

for i in range(1,5):
    for j in range(1,5):
        if(j%2==0):
            print("$",end = " ")
        else:
            print("#", end=" ")
    print()
        