# from .linked_list_node_double import LinkedListNodeDouble as Node  # TODO: May want to refactor to dynamically use single or double link node
from .linked_list import LinkedList

class Stack(object):

    def __init__(self):
        self.linked_list = LinkedList()

    def push(self, value):
        self.linked_list.push(value)

    def pop(self):
        return self.linked_list.remove_head()
    
    def peek(self):
        return self.linked_list.head

    def is_empty(self):
        return self.linked_list.is_empty()
    
    def __str__(self):
        return "[{}]".format(self.linked_list.head)
     