from math import sqrt

def distance(x1,y1,x2,y2):
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
a = float(input())
b = float(input())
c = float(input())
d = float(input())
print(distance(a,b,c,d))