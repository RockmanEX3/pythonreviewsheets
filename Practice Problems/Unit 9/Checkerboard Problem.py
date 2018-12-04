dimensions = [int(i) for i in input().split()]
checkerboard = [["."] * dimensions[1] for i in range(0,dimensions[0])]

for i in range(0,dimensions[0]):
    for j in range(0,dimensions[1]):
        if (i+j)%2 == 1:
            checkerboard[i][j] = "*"

for row in checkerboard:
    print(" ".join(row))
    