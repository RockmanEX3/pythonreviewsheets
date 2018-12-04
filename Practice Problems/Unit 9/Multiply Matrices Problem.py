given = [int(i) for i in input().split()]
A = []
B = []
for i in range(0,given[0]):
    A.append([int(j) for j in input().split()])
for i in range(0,given[1]):
    B.append([int(j) for j in input().split()])
    
C = []
for i in range(0,given[0]):
    C.append([0] * given[2])

def entry(i,k):
    s = 0
    for a in range(0,given[1]):
        s += (A[i][a] * B[a][k])
    return s

for i in range(0,given[0]):
    for k in range(0,given[2]):
        C[i][k] = str(entry(i,k))
        
for row in C:
    print(" ".join(row))
    
