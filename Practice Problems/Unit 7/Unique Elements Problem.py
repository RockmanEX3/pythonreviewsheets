list = [i for i in input().split()]
wanted = []
for i in range(0,len(list)):
    counter = 0
    for j in range(0,len(list)):
        if i != j and list[i] == list[j]:
            counter += 1
    if counter == 0:
        wanted.append(list[i])
print(" ".join(wanted))