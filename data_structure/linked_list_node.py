from .node import Node

class LinkedListNode(Node):
    
    def __init__(self, value):
        super().__init__(value)
        self.next = None

    def __str__(self):

        if self.next == None:
            return "{}".format(self.value)
        
        return "{} -> {}".format(self.value, self.next)  