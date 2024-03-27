
def bubble(ls):
    n = len(ls)-1
    for _ in range(0, n):
        for j in range(0, n):
            if ls[j] > ls[j+1]:
                ls[j],ls[j+1] = ls[j+1],ls[j]
    return ls



a = [1,3,7,8,0,3,4,43,2]
# [0, 1, 2, 3, 3, 4, 7, 8, 43]
print(bubble(a))

"""
uno de los algoritmo de mas simples de ordenacion.
o(n^2)
"""