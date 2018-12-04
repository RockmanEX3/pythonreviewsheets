d = [int(i) for i in input().split()]
m = []
for i in range(0,d[0]):
    m.append([j for j in input().split()])
w = [int(i) for i in input().split()]

def swap_columns(a,i,j):
    colA = []
    colB = []
    for k in range(0,len(a)):
        colA.append(a[k][i])
        colB.append(a[k][j])
    for k in range(0,len(a)):
        a[k][i] = colB[k]
        a[k][j] = colA[k]

swap_columns(m,w[0],w[1])

for row in m:
    print(" ".join(row))
        