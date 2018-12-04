givenInputs = input()
givenList = givenInputs.split(" ")
wantedList = []
for i in range(1,len(givenList)):
    if int(givenList[i]) > int(givenList[i-1]):
        wantedList.append(givenList[i])
print(" ".join(wantedList))