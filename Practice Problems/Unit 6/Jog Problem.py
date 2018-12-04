import math
x = int(input())
y = int(input())
print(math.ceil(math.log(y/x,1.1))+1)

#1.1^d * x = y
#log base 1.1 (y/x) = d