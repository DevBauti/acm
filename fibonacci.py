
# mini manejo de error 
while True:
    try: 
        n = int(input("escribe un numero:"))
        if n < 0:
            raise ValueError("no puede ser negativo")
        break
    except ValueError() as e :
        print(e)   


#ciclo while
def fib(n):
    a = [0,1]
    # rapido O(n)
    while len(a) < (n + 1):
        a.append(a[-1]+ a[-2])
    
    return a

# print(fib(n))


def fibo(n):
    a, b = 0, 1 
    # ridiculamente rapido O(n)
    for _ in range(n):
        a, b = b, a + b
    
    return a

# print(fibo(n))

def fibo_recur(n):
    # limpio pero costoso O(n^2)
    if n > 1:
        return fibo_recur(n-1) + fibo_recur(n-2)
    
    return n
    
print(fibo_recur(n))