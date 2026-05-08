class LowBalanceError(Exception):
    pass
class Account:
    balance = 4000
    def withdrawl(amount):
        if amount <= Account.balance:
            print(f"collect cash : {amount}")
            Account.balance = Account.balance - amount
        else:
            raise LowBalanceError("Low Balance")
        return
    
amt = int(input("Enter  withdrawl amt : "))
try :
    Account.withdrawl(amt)
except LowBalanceError as msg:
    print(f"Exception : {msg}")
print(f"Final Balance : {Account.balance}")