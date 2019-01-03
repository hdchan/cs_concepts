from enum import Enum

class EdgeType(Enum):
    DIRECTED = 0
    UNDIRECTED = 1
    
class GraphEdge(object):

    def __init__(self, source, target, weight = 1):
        self.source = source
        self.target = target
        self.weight = weight