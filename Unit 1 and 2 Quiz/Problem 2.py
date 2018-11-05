names = []
GPAs = []
for i in range(0,4):
    name = input("Type name: ")
    names.append(name)
    GPA = float(input("Type GPA: "))
    GPAs.append(GPA)
sum = 0
for i in range(0,4):
    sum += GPAs[i]
print("The average GPAs of " + names[0] + ", " + names[1] + ", " + names[2] + ", and " + names[3] + " is " + str(sum/4))