class Node(object):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "Node({})".format(self.value)