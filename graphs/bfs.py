
from collections import deque

#
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    result = []

    while queue:
        v = queue.popleft()
        result.append(v)
        for neigbour in graph[v]:
            if neigbour not in visited:
                queue.append(neigbour)
                visited.add(neigbour)
    return result

"""

"""

a = {'a':['b','c','d'],
     'b':['a','c','d'],
     'c':['a','d'],
     'd':['c','e','f'],
     'e':['a','c','f'],
     'f':['b','e']}



print(bfs(a, 'a'))
print(bfs(a, 'e'))