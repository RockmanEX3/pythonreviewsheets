import math

def prime(n):
    if n == 0 or n == 1:
        return False
    else:
        counter = 0
        for i in range(2,int(math.sqrt(n))+1):
            if n%i == 0:
                return False
        return True

a = int(input())
b = int(input())
for i in range(a+1,b):
    if prime(i) == True:
        print(i)