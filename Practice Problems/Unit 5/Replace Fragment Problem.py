s = input()
fh = s.find("h")
lh = s.rfind("h")

string = ""
for i in range(fh+1,lh):
    if s[i] == "h":
        string += "H"
    else:
        string += s[i]

print(s[0:fh+1] + string + s[lh:])