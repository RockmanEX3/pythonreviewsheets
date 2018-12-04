# Diagonal Problem 1

number = int(input())

for i in range(0,number):
    row = []
    for j in range(0,number):
        if j < i:
            row.append(str(i-j))
        else:
            row.append(str(j-i))
    print(" ".join(row))
    
# Diagonal Problem 2

n = int(input())

for i in range(0,n):
    row = []
    for j in range(0,n):
        if j < (n-1-i):
            row.append("0")
        elif j == (n-1-i):
            row.append("1")
        else:
            row.append("2")
    print(" ".join(row))