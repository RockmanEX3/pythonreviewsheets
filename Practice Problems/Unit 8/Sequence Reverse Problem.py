givenlist = []
while True:
  a = input()
  givenlist.append(a)
  if a == "0":
      break
for i in range(1,len(givenlist)+1):
  print(givenlist[len(givenlist)-i])