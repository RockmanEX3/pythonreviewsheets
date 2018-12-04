given = [int(i) for i in input().split()]
pins = ["I"] * given[0]

rolls = []
for i in range(0,given[1]):
    rolls.append(input())

for i in range(0,len(rolls)):
    attempt = [int(j) for j in rolls[i].split()]
    for k in range(attempt[0]-1,attempt[1]):
        pins[k] = "."
print("".join(pins))