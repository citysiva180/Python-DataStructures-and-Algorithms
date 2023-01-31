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

    # Adding vertex
    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    # Adding Edge
    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    # Remove Edge
    def remove_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
                return True
            except ValueError:
                pass
            return True
        return False

    # Removing Vertex
    def remove_vertex(self, vertex):
        if vertex in self.adj_list.keys():
            for other_vertex in self.adj_list[vertex]:
                self.adj_list[other_vertex].remove(vertex)
                del self.adj_list[vertex]
                return True
            return False


my_graph = Graph()


my_graph.add_vertex("A")
my_graph.add_vertex("B")
my_graph.add_vertex("C")
my_graph.add_vertex("D")

my_graph.add_edge("A", "B")
my_graph.add_edge("B", "C")
my_graph.add_edge("C", "A")

my_graph.remove_edge("A", "B")
my_graph.remove_edge("A", "D")

my_graph.print_graph()

my_graph.remove_vertex("D")

my_graph.print_graph()
