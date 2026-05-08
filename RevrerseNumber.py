num = 2345
rev = 0
while num > 0:
    digit = num % 10  # take last digit
    rev = rev * 10 + digit 
    num = num // 10  # remove the last digit
print(rev)