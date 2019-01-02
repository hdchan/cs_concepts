from .binary_tree import BinaryTree

class BinarySearchTree(BinaryTree):

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if node == None:
            return self._create_node_for(value)

        if value < node.value:
            node.left = self._insert(node.left, value)
        else:
            node.right = self._insert(node.right, value)
            
        return node