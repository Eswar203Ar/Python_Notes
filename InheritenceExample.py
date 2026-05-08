class First:
    def m1():
        print("First -m1")
        return
class Second(First):
    def m2():
        print("Second - m2")
        return
Second.m2()
Second.m1()
    