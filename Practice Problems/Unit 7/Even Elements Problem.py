givenInputs = input()
givenList = givenInputs.split(" ")
wantedList = []
for i in range(0,len(givenList)):
    if int(givenList[i])%2 == 0:
        wantedList.append(givenList[i])
print(" ".join(wantedList))