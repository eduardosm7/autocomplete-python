class Node:

    def __init__(self, item=None, prev=None, nex=None):
        self.item = item
        self.prev = prev
        self.nex = nex
    

class List:

    def __init__(self):
        self.first = self.last = Node()
        self.size = 0
    
    def get_size(self):
        return self.size

    def insert_ordered(self, item, cmp, rev=False):
        if self.get_size() == 0:
            self.first.nex = Node(item, self.first, self.last)
            self.last.prev = self.first.nex
            self.size += 1
        else:
            aux = self.first.nex
            if rev:
                while aux != self.last and cmp(item, aux.item) <= 0:
                    aux = aux.nex
            else:
                while aux != self.last and cmp(item, aux.item) >= 0:
                    aux = aux.nex
            aux.prev.nex = Node(item, aux.prev, aux)
            aux.prev = aux.prev.nex
            self.size += 1

    def remove_end(self):
        if self.get_size() != 0:
            self.last.prev.prev.nex = self.last
            self.last.prev = self.last.prev.prev
            self.size -= 1

    def __str__(self):
        result = ""
        aux = self.first.nex
        while aux != self.last and aux is not None:
            result += str(aux.item) + '\n'
            aux = aux.nex
        return result

    def __repr__(self):
        return self.__str__()
