class test:
    def abc():
        print("Static method")
        return
    def xyz(self):
        print("Dynamic / instance method")
        return
    def __init__(self):
        print("Constructor")
test.abc()
t = test()
t.xyz()