class Employee:
    def __init__(self,num,name,salary):
        self.num = num
        self.name = name
        self.salary = salary
        return
    def details(self):
        print(f"{self.num} , {self.name} , {self.salary}")
        return
e1 = Employee(101 , "Ravi" , 45000)
e2 = Employee(102 , 'Ramesh' , 40000)
e3 = Employee(103 , "Raju" , 35000)
e1.details()
e2.details()
e3.details()