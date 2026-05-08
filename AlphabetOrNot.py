## Write a program to read character and check alphabet or not
ch = input("Enter the charcter : ")

if (ch >= 'A' and ch <= 'Z') or (ch >= 'a' and ch <= 'z'):
    print("It is an Alphabet")
else:
    print("It is NOT an Alphabet")