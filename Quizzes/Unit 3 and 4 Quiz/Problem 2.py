a = int(input())
b = int(input())
c = int(input())
if a < b and b < c:
    print("YES")
else:
    print("NO")
    if a < b and a < c:
        print(a)
        print(c)
        print(b)
    elif b < a and b < c:
        print(b)
        if a < c:
            print(a)
            print(c)
        else:
            print(c)
            print(a)
    else:
        print(c)
        if b < a:
            print(b)
            print(a)
        else:
            print(a)
            print(b)