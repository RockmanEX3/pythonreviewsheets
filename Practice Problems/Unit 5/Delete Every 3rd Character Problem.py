s = input()
wanted = ""
for i in range(0,len(s)):
    if i%3 != 0:
        wanted += s[i]
print(wanted)