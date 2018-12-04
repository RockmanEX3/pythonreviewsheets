a = input()
counter = 0
for i in range(0,len(a)):
    if a[i] == "f":
        counter += 1
if counter > 1:
    print(a.find("f"))
    print(a.rfind("f"))
elif counter == 1:
    print(a.find("f"))