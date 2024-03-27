

def selectionsort(ls):
    n = len(ls)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if ls[j] < ls[min_index]:
                min_index = j
        ls[i], ls[min_index] = ls[min_index], ls[i]
    return ls

a = [1,34,6,977,5,4]
#[1, 4, 5, 6, 34, 977]
print(selectionsort(a))

"""
es sumamente simple, parecido a bubble.
O(n^2)
"""