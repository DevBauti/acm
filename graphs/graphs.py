from ..search_short import quick_sort


#Grafo_ejemplo = {'s':['a','b','c'], 'a'['d','e','j'],...}
#clase de un grafo
class Directed_Graph:
    def __init__(self):
        self.graph_dict = {} #en si un diccionario
    
    def add_vertex(self, vertex):
        if vertex in self.graph_dict:
            return "Vertex already in graph"
        
        self.graph_dict[vertex] = []#
    
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
    
    def __str__(self) -> str:
        all_edges = ''                      #{s:[a,b,c,d]}
        for v1 in self.graph_dict:          #{s}-->[a],{s}-->[b]...
            for v2 in self.graph_dict[v1]:
                all_edges += v1.get_name() +'--->'+ v2.get_name()+'\n'
        return all_edges

#grafo no dirigido    
class Undirected(Directed_Graph):
    def add_edge(self, edge):
        
        super().add_edge(self, edge)
        #
        edge_back = Edge(edge.get_v2(), edge.get_v1())
        super().add_edge(self, edge_back)

#conecciones
class Edge:
    def __init__(self, v1,v2):
        self.v1 = v1
        self.v2 = v2
    
    def get_v1(self):
        return self.v1
    def get_v2(self):
        return self.v2
    
    #nota: __str__ esto es lo que invoca print
    def __str__(self) -> str :
        return self.v1.get_name() + '--->' + self.v2.get_name()

#nodos o vertices   
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
    for v in arr:
        g.add_vertex(Vertex(v))
    #
    g.add_edge(Edge(g.get_vertex(),g.get_vertex()))# inplementar una conexion randomizada

G1 = build_graph(Directed_Graph,arr=quick_sort() ) 

# def data():
#     arr = quick_sort()
#     a = len(arr) // 2
#     return arr
