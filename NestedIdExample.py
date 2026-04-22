## chexk if the number divisble by 7 (only if the number is positive or negative)
num = int(input("Enter the number"))
if(num>0):
    if(num%7==0):
        print("Number divisble by 7")
    else:
        print("Number not divisible by 7")
    
else:
    print("Negative number")