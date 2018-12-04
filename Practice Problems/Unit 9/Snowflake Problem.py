n = int(input())
a = int((n-1)/2)

snowflake = []
for i in range(0,a):
    row = ["." for j in range(0,n)]
    row[0+i] = "*"
    row[n-1-i] = "*"
    row[a] = "*"
    snowflake.append(row)
snowflake.append(["*"] * n)
for i in range(0,a):
    row = ["." for j in range(0,n)]
    row[a-1-i] = "*"
    row[a+1+i] = "*"
    row[a] = "*"
    snowflake.append(row)
    
for row in snowflake:
    print(" ".join(row))