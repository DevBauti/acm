
while True:
    try:
        n = int(input("dame un numero: "))
        if n < 0:
            raise ValueError("El numero no puede ser negativo")
        break
    except ValueError() as e:
        print(e)



def coeficiente_binomial(n, k):
    if k == 0 or k == n:
        return 1
    return coeficiente_binomial(n-1, k-1) + coeficiente_binomial(n-1, k)

def bernoulli(n):
    if n == 0:
        return 1

    suma = int
    for k in range(n):
        suma += coeficiente_binomial(n + 1, k) * bernoulli(k)
    return -1 / (n + 1) * suma

print(bernoulli(n))