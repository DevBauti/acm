

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
Funciona con listas ordenadas, no olvidar

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
