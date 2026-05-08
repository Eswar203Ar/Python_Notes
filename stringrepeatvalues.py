s = "a3b2c5d4e3"
result = ""
ch = ""

for i in range(len(s)):
    if i % 2 == 0:          # even index → character
        ch = s[i]
    else:                   # odd index → number
        count = int(s[i])
        for j in range(count):
            result += ch

print(result)

        