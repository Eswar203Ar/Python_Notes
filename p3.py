class Test:
    def m1():
        print("static method")
        return
    
    def m2(self):
        print("Dynamic method")
        return

Test.m1()
obj = Test()
obj.m2()