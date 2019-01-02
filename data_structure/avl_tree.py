from .binary_search_tree import BinarySearchTree
from .avl_tree_node import AVLTreeNode

class AVLTree(BinarySearchTree):

    def _insert(self, node, value):
        if node == None:
            return self._create_node_for(value)

        if value < node.value:
            node.left = self._insert(node.left, value)
        else:
            node.right = self._insert(node.right, value)
            
        balanced_node = self._balanced(node)
        balanced_node.height = max(balanced_node.left_height(), balanced_node.right_height()) + 1
        return balanced_node
        

    def _balanced(self, node):
        if node.balance_factor() == 2:
            if node.left != None and node.left.balance_factor() == -1:
                return self._left_right_rotate(node)
            else:
                return self._right_rotate(node)
        elif node.balance_factor() == -2:
            if node.right != None and node.right.balance_factor() == 1:
                return self._right_left_rotate(node)
            else:
                return self._left_rotate(node)
        else:
            return node

    # https://medium.com/@henry.d.chan/binary-tree-rotations-7722027dd8a1
    # rotation only needs to happen on the bottom most node containing the invalid balance factor
    def _left_rotate(self, node):
        pivot = node.right
        node.right = pivot.left
        pivot.left = node

        # adjust height
        node.height = max(node.left_height(), node.right_height()) + 1
        pivot.height = max(pivot.left_height(), pivot.right_height()) + 1

        return pivot # this node will get reconnected to the rest of the tree

    def _right_rotate(self, node):
        pivot = node.left
        node.left = pivot.right
        pivot.right = node

        # adjust height
        node.height = max(node.left_height(), node.right_height()) + 1
        pivot.height = max(pivot.left_height(), pivot.right_height()) + 1

        return pivot # this node will get reconnected to the rest of the tree

    def _right_left_rotate(self, node):
        if node.right == None:
            return node
        
        node.right = self._right_rotate(node.right)
        return self._left_rotate(node)
    
    def _left_right_rotate(self, node):
        if node.left == None:
            return node
        
        node.left = self._left_rotate(node.left)
        return self._right_rotate(node)

    def _create_node_for(self, value):
        return AVLTreeNode(value)