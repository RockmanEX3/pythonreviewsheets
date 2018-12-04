# Clock Face Problem 1

H = int(input())
M = int(input())
S = int(input())

print((H*30)+(M*0.5)+(S*(0.5/60)))

# Clock Face Problem 2

alpha = float(input())
#30 deg --> 60 min, so 1 deg --> 2 min
totminutes = 2 * alpha
relminutes = totminutes%60
#60 min --> 360 deg, so 1 min --> 6 deg
print(relminutes*6)