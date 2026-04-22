## Read the charcter is uppercase/lowercase/digit or symbols
ch = input("Enter charcters : ")
if(ch>='A' and ch <='Z'):
    print("Uppercase letters")
elif(ch >='a' and ch <='z'):
    print("Lowercase letters")
elif(ch>='0' and ch<='9'):
    print("Digits")
else:
    print("Symbols")