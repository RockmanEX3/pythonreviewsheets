# Sum of 10 Numbers

sum = 0
for i in range(0,10):
    sum += int(input())
print(sum)

# Sum of N Numbers

N = int(input())
sum = 0
for i in range(0,N):
    sum += int(input())
print(sum)

# Sum of Cubes

n = int(input())
sum = 0
for i in range(1,n+1):
    sum += i**3
print(sum)

# Sum of Factorials

sum = 0
for i in range(1,int(input())+1):
    product = 1
    for j in range(1,i+1):
        product*=j
    sum += product
print(sum)