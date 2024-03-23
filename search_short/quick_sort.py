

ls = input("agrega la entrada: ")

# O(n log n) / peor de los casos O(n^2)

def Quick_sort(ls):
    #0 o 1 return []
    if len(ls) <= 1:
        return ls
    
    # punto intermedio
    pivot = ls[len(ls)//2] 
    
    #dividir la lista en dos
    left = [x for x in ls if x < pivot]
    middle = [x for x in ls if x == pivot]
    right = [x for x in ls if x > pivot]
    
    #llamar recursivamente y retornar ordenado
    return Quick_sort(left) + middle + Quick_sort(right)


print(Quick_sort(ls))

"""
print(Quick_sort([123,456,177182,19]))
#[19, 123, 456, 177182]

print(Quick_sort('hagsaioxkkkkkknasbavd'))
#['a', 'a', 'a', 'a', 'b', 'd', 'g', 'h', 'i', 'k', 'k', 'k', 'k', 'k', 'k', 'n', 'o', 's', 's', 'v', 'x']

print(Quick_sort(lorem ipsum))
#[' ', 'e', 'i', 'l', 'm', 'm', 'o', 'p', 'r', 's', 'u']

Okey esto es genial, se puede mejorar con regex
"""
