# Fibonacci Number

a = 0
b = 1
n = int(input())

if n == 0 or n == 1:
    if n == 0:
        print(0)
    else:
        print(1)
else:
    for i in range(0,n-1):
        stock = a+b
        a = b
        b = stock
    print(b)
    
# Fibonacci Index

a = 0
b = 1
n = int(input())
counter = 2

while n>b:
    stock = a+b
    a = b
    b = stock
    counter += 1
if n == b:
    print(counter-1)
else:
    print(-1)