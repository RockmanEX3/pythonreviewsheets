a = input()
firstH = a.find("h")
lastH = a.rfind("h")
print(a[0:firstH] + a[lastH+1:])