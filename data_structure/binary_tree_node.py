from .node import Node
class BinaryTreeNode(Node):

    def __init__(self, value):
        super().__init__(value)
        self.left = None
        self.right = None

    def traverse_in_order(self, visit):
        if self.left != None:
            self.left.traverse_in_order(visit)
        
        visit(self)

        if self.right != None:
            self.right.traverse_in_order(visit)

    def traverse_pre_order(self, visit):
        visit(self)

        if self.left != None:
            self.left.traverse_pre_order(visit)

        if self.right != None:
            self.right.traverse_pre_order(visit)
        
    def traverse_post_order(self, visit):
        if self.left != None:
            self.left.traverse_post_order(visit)

        if self.right != None:
            self.right.traverse_post_order(visit)

        visit(self)

    def __str__(self):
        return self._diagram(self)

    def _diagram(self, node, top = "", root = "", bottom = ""):  
        if node == None:
            return "{}nil\n".format(root)

        if node.left == None and node.right == None:
            return "{}{}\n".format(root, node.value)

        first = self._diagram(node.right, "{} ".format(top), "{}┌──".format(top), "{}│ ".format(top))
        second = "{}{}\n".format(root, node.value)
        third = self._diagram(node.left, "{}│ ".format(bottom), "{}└──".format(bottom), "{} ".format(bottom))

        return "{}{}{}".format(first, second, third)