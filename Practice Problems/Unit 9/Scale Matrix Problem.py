d = [int(i) for i in input().split()]
M = []
for i in range(0,d[0]):
    M.append([int(j) for j in input().split()])
c = int(input())
for i in range(0,d[0]):
    for j in range(0,d[1]):
        M[i][j] = str(M[i][j] * c)

for row in M:
    print(" ".join(row))