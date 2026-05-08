class Person:
    def can_vote(age):
        if(age>= 18):
            print("Vote")
        else:
            print("not")
            
Person.can_vote(16)
"""
age = int(input("Enter a value:"))
obj = Person
obj.can_vote(age)
"""