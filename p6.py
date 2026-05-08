while True:
    n = int(input("Enter a num:"))
    for i in range(1,11):
        print(f"{n} * {i} = {n*i}")
    
    ch = input("Do you want to stop(yes/no) :")
    if ch == 'no':
        break
    


