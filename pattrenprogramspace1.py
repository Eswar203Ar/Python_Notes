for i in range(1,6):
    for k in range(1,6-i):
        print(" ",end = " ")
    for j in range(i,0,-1):
        print(j,end=" ")
    print()