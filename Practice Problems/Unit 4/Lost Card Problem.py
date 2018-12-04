list =[]
a = int(input())+1
for i in range(1,a-1):
    list.append(int(input()))
    
lostcard = 0
for i in range(1,a):
    if i not in list:
        lostcard = i
print(lostcard)