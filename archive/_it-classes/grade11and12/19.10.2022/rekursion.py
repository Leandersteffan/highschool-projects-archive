def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def mult(z1, z2):
    if z1 == 0 or z2 == 0:
        return 0
    elif z2 == 1:
        return z1
    else:
        return z1 + mult(z1, z2 - 1)

def pot(b, e):
    if e == 0:
        return 1
    elif b == 0:
        return 0
    elif e == 1:
        return b
    else:
        return b * pot(b, e - 1)


print(fib(6))
print(mult(2, 10))
print(pot(2, 8))
