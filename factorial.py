

n = int(input())

def f(n):
    r = 1
    for i in range(1, n+1):
        r *= i
    return r   

print(f(n))

def fa(n):
    r = 1
    i = 1
    while i <= n:
        r *= i
        i+=1
    return r

print(fa(n))

def fac(n):
    if n == 0:
        return 1
    return n * fac(n-1)

# print(fact(n))

#es un ejemplo simple sobre recursividad