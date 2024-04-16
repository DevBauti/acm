
# 
class Nodo:
    def __init__(self, value):
        self.value = value
        self.contiguos = None

# 
class LikedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_nodo = Nodo(value)
        new_nodo.contiguos = self.head
        self.head = new_nodo

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=' -> ')
            current = current.contiguos
        print('None')


ls = LikedList()
ls.insert(3)
ls.insert(2)
ls.insert(1)
ls.print_list()