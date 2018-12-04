list = [int(i) for i in input().split()]
max = max(list)
maxindex = list.index(max)
min = min(list)
minindex = list.index(min)
list[minindex] = max
list[maxindex] = min
for i in range(0,len(list)):
    list[i] = str(list[i])
print(" ".join(list))