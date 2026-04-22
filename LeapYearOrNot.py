## check wheather the given year is leap year or not
# if the number is divisble by 400
# if the number is divible by 4 and not divisble by 100
year = int(input("Enter year :"))
if(year%400==0):
    print("Leap Year")
elif(year%4==0 and year%100!=0):
    print("Leap Year")
else:
    print("Not a leap year")