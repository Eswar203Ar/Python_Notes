## even number count by using function
def even_count(n):
    count = 0
    for i in range(1,11):
        if(n%2==0):
            count+=1
    print(f"even count is : {count}")
    return

even_count(10)