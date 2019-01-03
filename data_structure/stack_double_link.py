from .stack import Stack
from .linked_list_double import LinkedListDouble

class StackDoubleLink(Stack):

    def __init__(self):
        self.linked_list = LinkedListDouble()