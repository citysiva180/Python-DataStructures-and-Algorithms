# Graphs
# Vertex or node is the area where the data is stored but in this, you have edges. Which is the lines connecting these nodes.
# So there are multiple ways to connect to a node, which increases the possibility to have shortest path in terms of search
# You could have a bi-directional or a single directional way of connecting.

# SO we have 2 different type of graph approaches.
# A Graph Adjacency Matrix
# A Graph Adjacency List

class Graph:
    def __init__(self):
        self.adj_list = {}

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ':', self.adj_list[vertex])

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False


my_graph = Graph()
my_graph.add_vertex("A")
my_graph.print_graph()
