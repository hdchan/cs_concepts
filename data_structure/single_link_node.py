from .node import Node

class SingleLinkNode(Node):
    
    def __init__(self, value):
        super().__init__(value)
        self.next = None
        
    def append_node(self, node):
        self.next = node

    def __str__(self):

        if self.next == None:
            return "{}".format(self.value)
        
        return "{} -> {}".format(self.value, self.next)  