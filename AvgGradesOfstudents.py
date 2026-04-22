## Check wheather the students avg grade marks
m1 = int(input("Enter m1 :"))
m2 = int(input("Enter m2 :"))
m3 = int(input("Enter m3 :"))
if(m1>=40 and m2>= 40 and m3>=40):
    avg = (m1+m2+m3)/3
    if(avg>=75):
        print("Get Distinction")
    elif(avg>=60):
        print("First class")
    elif(avg>=50):
        print("Second class")
    else:
        print("Third class")
else:
    print("Failed")