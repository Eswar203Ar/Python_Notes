for i in range(1,10):
    for j in range(1,10):
        if(i==9 or j==1 or i==1 or i==5):
            print("*",end=" ")
        else:
            print(" " , end = " ")
    print()