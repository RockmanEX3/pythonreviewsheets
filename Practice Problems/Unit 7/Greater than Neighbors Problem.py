givenList = [int(i) for i in input().split()]
counter = 0
for i in range(1,len(givenList)-1):
    if givenList[i] > givenList[i-1] and givenList[i] > givenList[i+1]:
        counter += 1
print(counter)