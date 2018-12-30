from .double_link_node import DoubleLinkNode as Node
from .linked_list_base import LinkedListBase

class Queue(LinkedListBase):
            
    def enqueue(self, value):
        new_node = Node(value)
        self._enqueue(new_node)

    def _enqueue(self, node):
        if (self.head_node == None):
            self.head_node = node
            self.tail_node = node
        else:
            self.tail_node.append_node(node)
            self.tail_node = node
        
        self.node_count += 1
        
    def dequeue(self):
        if (self.node_count == 0):
            raise Exception("There's nothing to dequeue!")
            
        dequeued_node = self.head_node
        self.head_node = dequeued_node.next
        if (self.head_node != None):
            self.head_node.previous = None
        self.node_count -= 1
        return dequeued_node
        