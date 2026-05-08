class Address:
    def __init__(self,street,city,state):
        self.street = street
        self.city = city
        self.state = state
        return
    def details():
        return f"{self.street},{self.city}.{self.state}"
        return
    
class Employee:
    def __init__(self,num,name,salary,addr):
        self.num = num
        self.name = name
        self.salary = salary
        self.addr = addr
    def details(self):
        print(f"{self.num},{self.name},{self.salary},{self.addr.details()}")
        return

addr = Address('KPHB','Hyderabad','Telengana')
e = Employee(101,'Amar',2500,addr)
e.details()