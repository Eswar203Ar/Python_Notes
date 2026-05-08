## Print table by using for loop in oops concept
class demo:
    def table(n):
        for i in range(1,11):
            print(f"{n} * {i} = {n*i}")
                 
demo.table(5)