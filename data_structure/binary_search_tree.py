from .binary_tree_node import BinaryTreeNode as Node

class BinarySearchTree(object):

    def __init__(self, value = None):
        if (value != None):
            self.root = Node(value)
        else:
            self.root = None
    
    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if (node == None):
            return Node(value)

        if (value < node.value):
            node.left = self._insert(node.left, value)
        else:
            node.right = self._insert(node.right, value)
            
        return node

    def __str__(self):
        if (self.root == None):
            return "empty tree"
        
        return "{}".format(self.root)