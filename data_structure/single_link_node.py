class SingleLinkNode(object):
    
    def __init__(self, value):
        self.value = value
        self.next = None
        
    def append_node(self, node):
        self.next = node

    def __str__(self):

        if (self.next == None):
            return "{}".format(self.value)
        
        return "{} -> {}".format(self.value, self.next)  