from .node import Node
from .graph_edge import EdgeType, GraphEdge

class GraphAdjacencyList(object):

    def __init__(self):
        self.adjacencies = {}

    def create_vertex(self, data):
        vertex = Node(data)
        self.adjacencies[id(vertex)] = []
        return vertex

    def add_directed_edge(self, source, target, weight):
        edge = GraphEdge(source, target, weight)
        self.adjacencies[id(source)].append(edge)

    def add_undirected_edge(self, first, second, weight):
        self.add_directed_edge(first, second, weight)
        self.add_directed_edge(second, first, weight)

    def add(self, edgeType, source, target, weight):
        if edgeType == EdgeType.DIRECTED:
            self.add_directed_edge(source, target, weight)
        elif edgeType == EdgeType.UNDIRECTED:
            self.add_undirected_edge(source, target, weight)

    def edges_for(self, source):
        adjacencies = self.adjacencies[id(source)]
        if adjacencies == None:
            return []
        return adjacencies

    def __str__(self):
        pass
    


    

