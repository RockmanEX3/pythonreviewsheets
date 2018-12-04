import math

a = int(input())
b = int(input())

sa = int(math.sqrt(a))
sb = int(math.sqrt(b))

for i in range(sa,sb+1):
    if i**2 >= a and i**2 <= b:
        print(i**2)