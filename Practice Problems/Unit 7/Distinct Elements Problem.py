list = [int(i) for i in input().split()]
distinct = []
counter = 0
for i in list:
    if i not in distinct:
        distinct.append(i)
        counter += 1
print(counter)