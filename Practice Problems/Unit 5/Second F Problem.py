a = input()
if a.find("f") == -1:
    print(-2)
else:
    b = a.find("f")
    print(a.find("f",b+1))