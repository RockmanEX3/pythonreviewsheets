a = input()

firstH = a.find("h")
lastH = a.rfind("h")

b = a[firstH:lastH+1]

print(a[0:firstH] + b[::-1] + a[lastH+1:])