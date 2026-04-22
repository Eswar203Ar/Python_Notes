## print table by using function
def table(n):
    for i in range(1,11):
        print(f"{n} * {i} = {n*i}")
    print( )
    return
table(5)
table(10)
table(15)
table(20)