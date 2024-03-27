

def insertion(ls):
    for i in range(1,len(ls)):
        current_value = ls[i]
        position = i
    
        while position > 0 and ls[position - 1] > current_value:
            ls[position] = ls[position-1]
            position-=1
        ls[position] = current_value
    return ls


a = [1,83,92,4,9,77,3]
print(insertion(a))
"""
super simple de comprender
O(n^2)
"""