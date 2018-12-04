str = input()
wanted = ""
for i in range(0,len(str)):
    if i%2 == 0:
        wanted += str[i]
print(wanted)