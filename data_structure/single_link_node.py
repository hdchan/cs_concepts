class SingleLinkNode(object):
    
    def __init__(self, value):
        self.value = value
        self.next_node = None
        
    def append_node(self, node):
        self.next_node = node
        self.next_node.previous_node = self

    def __str__(self):

        if (self.next_node == None):
            return "{}".format(self.value)
        
        return "{} -> {}".format(self.value, self.next_node)  