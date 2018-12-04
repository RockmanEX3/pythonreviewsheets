s = input()
string = ""
for i in range(0,len(s)):
    if s[i] != "@":
        string += s[i]
print(string)