## Keyword argument function
## We have to pass the aruguments by using the names as keyword
## we can pass the value any order
def keyword(name , age):
    print(f"Name : {name}  , Age : {age}")
    return
keyword("Eswar" , 24)
keyword(21 , "sailaja")
keyword(name = "sharika" , age = 25)