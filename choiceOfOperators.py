## hoice of Addition,sub,mult,div,quit
while True:
    print("1 . Addition")
    print("2 . subtract")
    print("3 . Multiply")
    print("4 . Quit")
    choice = int(input("Selection options:"))
    if(choice == 1):
        a = int(input("First number :"))
        b = int(input("Second number:"))
        print(f"sum = {a+b}")
    elif(choice == 2):
        a = int(input("First number :"))
        b = int(input("Second number:"))
        print(f"Differnce = {a-b}")
    elif(choice == 3):
        a = int(input("First number :"))
        b = int(input("Second number:"))
        print(f"Multiply = {a*b}")
    elif(choice == 4):
        print("End of the program")
        break
    else:
        print(f"Error : Ivalid choice")