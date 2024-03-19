

ls = input('agrega la entrada: ')

#ordenar la lista
def merge(left, right):
    #
    result = []
    i, j = 0, 0
    #mientras que i y j sea menor a la longitud
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    #juntamos las cosas
    result.extend(left[i:])
    result.extend(right[j:])
    return result

#
def mergesort(ls):
    #devuelve directamente
    if len(ls) <= 1:
        return ls
    #dividir la lista en dos mitades
    mid = len(ls) // 2
    #llamar recursivamente a mergesort en cada mitad
    left = mergesort(ls[:mid])
    right = mergesort(ls[mid:])
    #retorna la lista ordenada
    return merge(left, right)

print(mergesort(ls))

"""

print(mergesort("lorem ipsum"))
[' ', 'e', 'i', 'l', 'm', 'm', 'o', 'p', 'r', 's', 'u']
print(mergesort("pipo is a dog"))
[' ', ' ', ' ', 'a', 'd', 'g', 'i', 'i', 'o', 'o', 'p', 'p', 's']

Esto se puede mejorar mucho si se aplica regex
"""
