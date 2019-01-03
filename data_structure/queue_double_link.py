from .linked_list_double import LinkedListDouble
from .queue import Queue

class QueueDoubleLink(Queue):
            
    def __init__(self):

        self.linked_list = LinkedListDouble()