N = int(input())
i = 0
while 2**i <= N:
    i += 1
print(str(i-1) + " " + str(2**(i-1)))