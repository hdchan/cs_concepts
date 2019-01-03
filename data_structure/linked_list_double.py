from .linked_list_node_double import LinkedListNodeDouble
from .linked_list import LinkedList

class LinkedListDouble(LinkedList):

    def append(self, value):
        new_node = self._create_node_for(value)
        current_node = self.head
        if current_node == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.node_count += 1
    
    def push(self, value):
        new_node = self._create_node_for(value)
        previous_head = self.head
        if previous_head != None:
            previous_head.previous = new_node
        self.head = new_node
        self.head.next = previous_head
        self.node_count += 1
        
    def remove_head(self):
        head = self.head
        if head != None:
            if head.next == None:
                self.head = None
                self.tail = None
            else:
                self.head = head.next
                self.head.previous = None

            self.node_count -= 1
            return head

    def remove_tail(self):
        tail = self.tail
        if tail == self.head:
            return self.remove_head()
        elif tail != None:
            previous_tail = self.tail
            self.tail = self.tail.previous
            previous_tail.previous = None

            self.node_count -= 1
            return previous_tail

    def _create_node_for(self, value):
        return LinkedListNodeDouble(value)