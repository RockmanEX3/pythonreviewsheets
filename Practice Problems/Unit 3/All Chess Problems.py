# Rook

c1 = int(input())
r1 = int(input())
c2 = int(input())
r2 = int(input())
if c1==c2 or r1==r2:
    print("YES")
else:
    print("NO")
    
# Chess Square

c1 = int(input())
r1 = int(input())
c2 = int(input())
r2 = int(input())
if (c1+r1)%2 == (c2+r2)%2:
    print("YES")
else:
    print("NO")
    
# King

c1 = int(input())
r1 = int(input())
c2 = int(input())
r2 = int(input())
if abs(c1-c2)<=1 and abs(r1-r2)<=1:
    print("YES")
else:
    print("NO")

# Bishop

c1 = int(input())
r1 = int(input())
c2 = int(input())
r2 = int(input())
if abs(c1-c2) == abs(r1-r2):
    print("YES")
else:
    print("NO")
    
# Queen

c1 = int(input())
r1 = int(input())
c2 = int(input())
r2 = int(input())
if abs(c1-c2) == abs(r1-r2):
    print("YES")
else:
    if c1==c2 or r1==r2:
        print("YES")
    else:
        print("NO")

# Knight

c1 = int(input())
r1 = int(input())
c2 = int(input())
r2 = int(input())
if abs(c1-c2) == 2 and abs(r1-r2) == 1:
    print("YES")
elif abs(c1-c2) == 1 and abs(r1-r2) == 2:
    print("YES")
else:
    print("NO")