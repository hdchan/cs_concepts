from .linked_list_node import LinkedListNode as Node

class LinkedList(object):
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.node_count = 0
    
    def append(self, value):
        new_node = self._create_node_for(value)
        previous_tail = self.tail
        if previous_tail == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.node_count += 1
    
    def push(self, value):
        new_node = self._create_node_for(value)
        previous_head = self.head
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
                    
            self.node_count -= 1
            return head

    def remove_tail(self):
        tail = self.tail
        if tail == self.head:
            return self.remove_head()
        elif tail != None:
            current_node = self.head.next
            previous_node = self.head
            while (current_node.next != None):
                current_node = current_node.next
                previous_node = previous_node.next
            self.tail = previous_node
            self.tail.next = None
            self.node_count -= 1
            return current_node
        
    def node_at_index(self, idx):
        if self.node_count == 0:
            raise Exception("List is empty.")
        current_node = self.head
        counter = 0
        if counter == idx: 
            return current_node
    
        while (current_node.next != None):
            current_node = current_node.next
            counter += 1
            if counter == idx:
                return current_node
            
        raise Exception("Index {} out of bounds".format(idx))
        
    def is_empty(self):
        return self.node_count == 0

    def _create_node_for(self, value):
        return Node(value)
    
    def __str__(self):
        return "[{}]".format(self.head)