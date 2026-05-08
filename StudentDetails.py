class student:
    def __init__(self,name,course,fee):
        self.name = name
        self.course = course
        self.fee = fee
        return
    def Details(self):
        print(f"{self.name} , {self.course} , {self.fee}")
        return
    
s1 = student('Eswar' , 'Data Analyst' , 5000 )
s2 = student('Prasad' , ".Net" , 20000)
s3 = student('surendra' , 'Java' , 25000)
s1.Details()
s2.Details()
s3.Details()