class Find():
    def biggest(a,b,c):
        if(a>b and a>c):
            return a
        elif(b>c):
            return b
        else:
            return c
    
a,b,c = 15,35,20
big = Find.biggest(a,b,c)
print(big)