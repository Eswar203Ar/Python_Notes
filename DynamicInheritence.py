class First:
    def m1(self):
        print("First - m1")
        return
class Second(First):
    def m2(First):
        print("Second - m2")
        return
obj = Second()
obj.m1()
obj.m2()