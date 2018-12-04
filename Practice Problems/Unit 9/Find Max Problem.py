given = [int(item) for item in input().split()]

array = []
for i in range(0,given[0]):
    row = [int(item) for item in input().split()]
    array.append(row)

indexi = 0
indexj = 0
for i in range(0,given[0]):
    for j in range(0,given[1]):
        if array[i][j] > array[indexi][indexj]:
            indexi = i
            indexj = j
print(str(indexi) + " " + str(indexj))