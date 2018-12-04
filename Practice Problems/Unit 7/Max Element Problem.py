givenInputs = input()
givenList = givenInputs.split(" ")
for i in range(0,len(givenList)):
    givenList[i] = int(givenList[i])
largest = max(givenList)
print(str(largest) + " " + str(givenList.index(largest)))