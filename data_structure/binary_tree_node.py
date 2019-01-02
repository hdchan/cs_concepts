from .node import Node
class BinaryTreeNode(Node):

    def __init__(self, value):
        super().__init__(value)
        self.left = None
        self.right = None

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