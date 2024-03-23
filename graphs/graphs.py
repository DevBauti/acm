import random

#Grafo_ejemplo = {'s':['a','b','c'], 'a'['d','e','j'],...}
#clase de un grafo
class Directed_Graph:
    def __init__(self):
        self.graph_dict = {} #en si un diccionario
    
    def add_vertex(self, vertex):
        if vertex in self.graph_dict:
            return "Vertex already in graph"
        self.graph_dict[vertex] = [] #Inicialmente sin conexiones
    
    def add_edge(self, edge):
        v1 = edge.get_v1()
        v2 = edge.get_v2()

        if v1 not in self.graph_dict:
            raise ValueError(f'Vertex {v1.get_name()} not in graph')
        if v2 not in self.graph_dict:
            raise ValueError(f'Vertex {v2.get_name()} not in graph')
        self.graph_dict[v1].append(v2)

    def is_vertex_in(self, vertex):
        return vertex in self.graph_dict
    
    def get_vertex(self, vertex_name):
        for v in self.graph_dict:
            if vertex_name == v.get_name():
                return v
        print(f'Vertex {vertex_name} does not exist')

    def get_children(self, vertex):
        return self.graph_dict[vertex]

   #nota: __str__ esto es lo que invoca print
    def __str__(self) -> str:
        all_edges = ''                      #{s:[a,b,c,d]}
        for v1 in self.graph_dict:          #{s}-->[a],{s}-->[b]...
            for v2 in self.graph_dict[v1]:
                all_edges += v1.get_name() +'--->'+ v2.get_name()+'\n'
        return all_edges

#grafo no dirigido    
class Undirected(Directed_Graph):
    def add_edge(self, edge):
        super().add_edge(edge)
        edge_back = Edge(edge.get_v2(), edge.get_v1())
        super().add_edge(edge_back)

#Conexiones entre nodos
class Edge:
    def __init__(self,v1,v2):
        self.v1 = v1 
        self.v2 = v2
    
    def get_v1(self):
        return self.v1
    def get_v2(self):
        return self.v2
    
    def __str__(self):
        return self.v1.get_name() + '--->' + self.v2.get_name()

#Nodos o vertices   
class Vertex:
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        return self.name
    
    def __str__(self) -> str:
        return self.name
    
    
#constructor
def build_graph(graph, arr):
    g = graph()
    #agregar todos los nodos al grafo
    for v in arr:
        g.add_vertex(Vertex(v))   
    #
    g.add_edge(Edge(g.get_vertex('a'), g.get_vertex('b')))
    g.add_edge(Edge(g.get_vertex('a'), g.get_vertex('c')))
    g.add_edge(Edge(g.get_vertex('a'), g.get_vertex('d')))
    g.add_edge(Edge(g.get_vertex('b'), g.get_vertex('c')))
    g.add_edge(Edge(g.get_vertex('b'), g.get_vertex('d')))
    g.add_edge(Edge(g.get_vertex('c'), g.get_vertex('d')))
    g.add_edge(Edge(g.get_vertex('d'), g.get_vertex('e')))
    g.add_edge(Edge(g.get_vertex('e'), g.get_vertex('a')))

    return g


# def qs(a):
#     if len(a) <= 1:
#         return a
#     p = a[len(a)//2]
#     l = [x for x in a if x < p]
#     m = [x for x in a if x == p]
#     r = [x for x in a if x > p]
#     return qs(l)+m+qs(r)

# arr = qs(input("Agrega los nodos: "))
arr = ['a','b','c','d','e']

directed_graph = build_graph(Directed_Graph, arr)
print("Grafo Dirigido Aleatorio:")
print(directed_graph)

undirected_graph = build_graph(Undirected, arr)
print("\nGrafo No Dirigido Aleatorio:")
print(undirected_graph)

"""
Esto no esta terminado... lo tengo que rehacer, pero es una aproximacion.
"""