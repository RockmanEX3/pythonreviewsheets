def exponent(a,n):
    if n == 0:
        return 1
    else:
        return a * exponent(a,n-1)

a = float(input())
b = int(input())
print(exponent(a,b))