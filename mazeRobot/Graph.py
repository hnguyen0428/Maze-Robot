class Node:
    def __init__(self, n, x, y):
        self.id = n
        self.pos = (x,y)
        self.neighbors = {}

    def __str__(self):
        return str(self.id) + ' pos: ' + str(self.pos) + ' neighbors: ' +
               str([x.id for x in self.neighbors])

    def add_neighbor(self, n, weight=0):
        self.neighbors[n] = weight

    def get_neighbors(self):
        return self.neighbors.keys()

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.neighbors[neighbor]

    def get_pos(self):
        return self.pos


class Graph:
    def __init__(self):
        self.nodes = {}
        self.num_nodes = 0

    def __iter__(self):
        return iter(self.nodes.values())

    def add_node(self, n, x, y):
        self.num_nodes = self.num_nodes + 1
        new_node = Node(n, x, y)
        self.nodes[n] = new_node
        return new_node

    def get_node(self, n):
        if n in self.nodes:
            return self.nodes[n]
        else:
            return None

    # Add an edge to the graph
    # Precondition: both src and dest are existing nodes in the graph
    def add_edge(self, src, dest, weight = 0):
        self.nodes[src].add_neighbor(self.nodes[dest], weight)
        self.nodes[dest].add_neighbor(self.nodes[src], weight)

    def get_nodes(self):
        return self.nodes.keys()
