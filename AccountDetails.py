class Account:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
        return
    def details(self):
        print(f"{self.name} , {self.balance}")
        return
    
    def get_balance(self):
        return self.balance
    
a1 = Account("Eswar" , 45000)
a2 = Account("Sailu" , 25000)
a1.details()
a2.details()
print(f"a1 Balance is : {a1.get_balance()}")
print(f"a2 balance is : {a2.get_balance()}")