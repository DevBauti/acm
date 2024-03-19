

#
def dfs(graph, start):
    visited = set()
    #colocar el nodo en la pila 
    stack = [start]

    #mientras la pila no este vacia
    while stack:
        vertex = stack.pop() #saca un nodo
        if vertex not in visited: 
            visited.add(vertex)
            stack.extend(graph[vertex]-visited) #
    # todos los caminos usados
    return visited

a = set()

print(a)
"""

"""