class LinkedListBase(object):
    
    def __init__(self):
        self.head_node = None
        self.tail_node = None
        self.node_count = 0
    
    def node_at_index(self, idx):
        if (self.node_count == 0):
            raise Exception("List is empty.")
        current_node = self.head_node
        counter = 0
        if (counter == idx): 
            return current_node
    
        while (current_node.next != None):
            current_node = current_node.next
            counter += 1
            if (counter == idx):
                return current_node
            
        raise Exception("Index {} out of bounds".format(idx))
        
    def is_empty(self):
        return self.node_count == 0
    
    def __str__(self):
        return "[{}]".format(self.head_node)