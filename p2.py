## def the function and check alphabet or not
def is_alphabet(ch):
    if(ch >= 'a' and  ch <= 'z' or ch >= 'A' or ch <= 'Z'):
        print("Alphabet")
    else:
        print("not alphabet")
ch = input("Enter a value:")        
is_alphabet(ch)