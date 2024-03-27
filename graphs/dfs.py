

#exploracion profunda
def dfs(graph, start, visited=None ):
    if visited is None:
        visited = set()
    visited.add(start)
    result = [start]

    for n in graph[start]:
        if  n not in visited:
            result.extend(dfs(graph, n, visited))

    return result


"""
busqueda en profundidad
"""
b = {'a':['b','c','e'],
     'b':['a','c','d'],
     'c':['b','d'],
     'd':['e','a','f','c'],
     'e':['g'],
     'f':['c','d','b'],
     'g':['e'],
     }

print(dfs(b, 'a'))
print(dfs(b, 'g'))
print(dfs(b, 'b'))
