'''
(1,4)
(1,6)
(7,4)
'''

def extractCoordinates(c):
    string = str(c)
    leftpart = string.find("(")
    midpart = string.find(",")
    rightpart = string.find(")")
    list = []
    list.append(float(string[leftpart+1:midpart]))
    list.append(float(string[midpart+1:rightpart]))
    return list
    
a = extractCoordinates(input("Type coordinates in form (x,y): "))
b = extractCoordinates(input("Type coordinates in form (x,y): "))
c = extractCoordinates(input("Type coordinates in form (x,y): "))

if a[0] == b[0]:
    x = c[0]
elif a[0] == c[0]:
    x = b[0]
else:
    x = a[0]
    
if a[1] == b[1]:
    y = c[1]
elif a[1] == c[1]:
    y = b[1]
else:
    y = a[1]
    
print("(" + str(x) + "," + str(y) + ")")


