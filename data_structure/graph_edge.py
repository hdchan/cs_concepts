from enum import Enum

class EdgeType(Enum):
    DIRECTED = 0
    UNDIRECTED = 1
    
class GraphEdge(object):

    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight