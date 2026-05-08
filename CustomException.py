## Custom Exception
class InvalidAgeError(Exception): ## Custom Exception
    pass ## Pass can use for empty class
class Person:
    def can_vote(age):
        if(age>=18):
            print("Person can vote")
        else:
            raise InvalidAgeError("Under age") ## We should create exception object and raise when problem occurs
        return
age = int(input("Enter age :"))
try :
    Person.can_vote(age)
except InvalidAgeError as msg: ## we need to handle exception while calling the method
    print(f"Exception : {msg}")
        