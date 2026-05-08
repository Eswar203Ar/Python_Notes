class Account:
    def __init__(self , balance):
        self.balance = balance
        return
    def get_balance(self):
        return self.balance
    
    def deposit(self,amount):
        self.balance = self.balance + amount
        return 
    
    def withdrawl(self , amount):
        if amount < self.balance:
            print(f"cash collect is : {amount}")
            self.balance = self.balance - amount
        else:
            print("Error : Low balance")
            
        return
    
acc = Account(5000)
print(f"Balance Amount is : {acc.get_balance()}")
acc.deposit(3000)
print(f"After deposit : {acc.get_balance()}")
acc.withdrawl(6000)
print(f"After Withdrawl is : {acc.get_balance()}")