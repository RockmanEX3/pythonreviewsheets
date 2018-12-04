a = float(input())
b = int(input())
def power(base,exp):
    if exp == 0:
        return 1
    elif exp > 0:
        n = 1
        for i in range(0,exp):
            n *= base
        return n
    else:
        n = 1
        for i in range(0,exp):
            n /= base
        return n
print(a**b)