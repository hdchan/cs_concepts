from .double_link_node import DoubleLinkNode as Node
from .linked_list_base import LinkedListBase

class Stack(LinkedListBase):

    def push(self, value):
        new_node = Node(value)
        self._push(new_node)

    def _push(self, node):
        if (self.head_node == None):
            self.head_node = node
            self.tail_node = node
        else:
            node.append_node(self.head_node)
            self.head_node = node
        
        self.node_count += 1
        
    def pop(self):
        if (self.node_count == 0):
            raise Exception("There's nothing to pop!")
        
        popped_node = None
        
        if (self.head_node == self.tail_node):
            popped_node = self.head_node
            self.head_node = None
            self.tail_node = None
        else:
            popped_node = self.head_node
            self.head_node = self.head_node.next
            self.head_node.previous = None
            
        self.node_count -= 1
        
        popped_node.next = None
        popped_node.previous = None
        
        return popped_node
    
    def peek(self):
        return self.head_node
    
    
     