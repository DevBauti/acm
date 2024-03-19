

ls = input('agrega la lista a buscar: ')
target = input('agrega lo que deseas buscar: ')

def binary_search(ls, target):
    left, right = 0, len(ls)-1 
    while left <= right:
        #rango de busqueda
        mid = (right + left) // 2
        #
        if ls[mid] < target:
            left = mid + 1
        elif ls[mid] > target:
            right = mid - 1
        else:
            return mid
    
    return -1

print(binary_search(ls, target))

"""
La busqueda es exacta, ni no coincide a la perfeccion devuelve -1

print(binary_search([12,13,45,88,64,3],3))
#-1 esto se da por que toma hasta el primero que encuentra, si no es, te da -1
print(binary_search('18712899asd','a'))
#8
print(binary_search(['as','sa','cc','ba','ss','aa'],'cc'))
#2
"""

def bsRecursive(ls, target, left, rigth):
    if left > rigth:
        return -1
    
    mid = (left + rigth) // 2

    if ls[mid] == target:
        return mid
    elif ls[mid] > target:
        return bsRecursive(ls, target,left, mid-1 )
    else:
        return bsRecursive(ls, target, mid+1, rigth)

def bs(ls, target):
    return bsRecursive(ls, target, 0, len(ls)-1)

"""
print(bs([12,31,45,123,879,9182,99,12],879))
#4
print(bs([12,31,45,123,879,9182,99,12],45))
#2
"""
