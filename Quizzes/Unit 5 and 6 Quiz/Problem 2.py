str = input()
let = str[0]
wanted = str[0]
for i in range(1,len(str)):
    if str[i] == let:
        wanted += "$"
    else:
        wanted += str[i]
print(wanted)
