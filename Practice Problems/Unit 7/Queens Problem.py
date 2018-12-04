queens = []
for i in range(0,8):
    queens.append(input())

counter = 0
for i in range(0,8):
    positionA = [k for k in queens[i].split()]
    for j in range(i+1,8):
        positionB = [n for n in queens[j].split()]
        if abs(int(positionA[0]) - int(positionB[0])) == abs(int(positionA[1]) - int(positionB[1])) or positionA[0] == positionB[0] or positionA[1] == positionB[1]:
            counter += 1


if counter == 0:
    print("NO")
else:
    print("YES")