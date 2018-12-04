givenInputs = input()
givenList = givenInputs.split(" ")
i = 1
while i < len(givenList):
    if int(givenList[i])*int(givenList[i-1]) > 0:
        print(givenList[i-1] + " " + givenList[i])
        break
    i += 1