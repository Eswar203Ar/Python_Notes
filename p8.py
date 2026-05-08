class Student:
    def __init__(self,num,name,course):
        self.num = num
        self.name = name
        self.course = course
        return
    def details(self):
        print(f"{self.num}, {self.name},{self.course}")
        return
    

s1 = Student(101, 'Amar' , 'DataScience')
s2 = Student(102,'Eswar' , 'Data Analyst')
s1.details()
s2.details()