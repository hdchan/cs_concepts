from .linked_list_node import LinkedListNode as Node
from .linked_list import LinkedList

class Queue(object):
            
    def __init__(self):
        self.linked_list = LinkedList()

    def enqueue(self, value):
        self.linked_list.append(value)
        
    def dequeue(self):
        return self.linked_list.remove_head()

    def peek(self):
        return self.linked_list.head

    def is_empty(self):
        return self.linked_list.is_empty()
    
    def __str__(self):
        return "[{}]".format(self.linked_list.head)