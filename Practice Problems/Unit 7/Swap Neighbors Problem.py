list = input().split()
for i in range(0,len(list),2):
    if i+1 <= len(list)-1:
        stocka = list[i]
        stockb = list[i+1]
        list[i] = stockb
        list[i+1] = stocka
print(" ".join(list))