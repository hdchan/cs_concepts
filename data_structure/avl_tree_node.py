from .binary_tree_node import BinaryTreeNode

class AVLTreeNode(BinaryTreeNode):

    def __init__(self, value = None):
        super().__init__(value)
        self.height = 0

    def balance_factor(self):
        # if this difference is greater than 1, then it's unbalanced
        return self.left_height() - self.right_height()

    def left_height(self):
        if self.left == None:
            return -1
        return self.left.height

    def right_height(self):
        if self.right == None:
            return -1
        return self.right.height