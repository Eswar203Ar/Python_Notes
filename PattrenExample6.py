## Display the rows and coulms can be increments like 1 to 9 and repeat 1 to 9
k = 1
for i in range(1,8):
    for j in range(1,8):
        print(k,end=" ")
        k = k+1
        if(k==10):
         k=1
    print()