from .node import Node
from .graph_edge import EdgeType, GraphEdge
from .queue import Queue
from .stack import Stack
class GraphAdjacencyList(object):

    def __init__(self):
        self.adjacencies = {}
        self.vertexies = {}

    def create_vertex(self, data):
        vertex = Node(data)
        self.adjacencies[id(vertex)] = []
        self.vertexies[id(vertex)] = vertex
        return vertex

    def add_directed_edge(self, source, target, weight):
        edge = GraphEdge(source, target, weight)
        self.adjacencies[id(source)].append(edge)

    def add_undirected_edge(self, first, second, weight):
        self.add_directed_edge(first, second, weight)
        self.add_directed_edge(second, first, weight)

    def add(self, edgeType, source, target, weight = 1):
        if edgeType == EdgeType.DIRECTED:
            self.add_directed_edge(source, target, weight)
        elif edgeType == EdgeType.UNDIRECTED:
            self.add_undirected_edge(source, target, weight)

    def edges_for(self, source):
        adjacencies = self.adjacencies[id(source)]
        if adjacencies == None:
            return []
        return adjacencies

    def weight_for(self, source, target):
        edges = self.edges_for(source)
        found_edge = None
        for edge in edges:
            if edge.target == target:
                found_edge = edge
                break
        if found_edge != None:
            return found_edge.weight
        return None

    def breadth_first_search(self, source, visit):
        # uses a queue
        queue = Queue()
        visited = []

        queue.enqueue(source)
        
        while queue.is_empty() == False:
            current_node = queue.dequeue().value
            
            visit(current_node)
            visited.append(current_node)

            edges = self.edges_for(current_node)
            
            for edge in edges:
                if edge.target not in visited:
                    visited.append(edge.target)
                    queue.enqueue(edge.target)
            
    def depth_first_search(self, source, visit):
        # uses a stack
        stack = Stack()
        visited = []

        stack.push(source)

        while stack.is_empty() == False:
            current_node = stack.pop().value

            visit(current_node)
            visited.append(current_node)

            edges = self.edges_for(current_node)

            for edge in edges:
                if edge.target not in visited:
                    visited.append(edge.target)
                    stack.push(edge.target)

    def __str__(self):
        result = ""
        for vertex, edges in self.adjacencies.items():
            edge_string = ""
            if len(edges) == 0:
                continue
            for idx, edge in enumerate(edges):
                if idx != len(edges) - 1:
                    edge_string = "{}{}, ".format(edge_string, edge.target)
                else:
                    edge_string = "{}{}".format(edge_string, edge.target)
            
            result = "{}{}  ---> [ {} ]\n".format(result, self.vertexies[vertex], edge_string)
        return result
    


    

