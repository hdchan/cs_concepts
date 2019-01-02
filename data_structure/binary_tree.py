from .binary_tree_node import BinaryTreeNode as Node

class BinaryTree(object):

    def __init__(self, value = None):
        if value != None:
            self.root = self._create_node_for(value)
        else:
            self.root = None

    def _create_node_for(self, value):
        return Node(value)

    def __str__(self):
        if self.root == None:
            return "empty tree"
        
        return "{}".format(self.root)