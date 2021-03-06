from .linked_list_node import LinkedListNode

class LinkedListNodeDouble(LinkedListNode):
    
    def __init__(self, value):
        super().__init__(value)
        self.previous = None
        
    def append_node(self, node):
        super().append_node(node)
        self.next.previous = self

    def __str__(self):

        if self.next == None:
            return "{}".format(self.value)
        
        return "{} <-> {}".format(self.value, self.next)  