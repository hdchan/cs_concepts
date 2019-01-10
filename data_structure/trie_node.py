class TrieNode(object):

    def __init__(self, key=None, parent=None):
        # value should be hashable
        self.key = key
        self.parent = parent # of TrieNode type
        self.children = {} # dictionary where key is key and value is node
        self.is_terminating = False

    # def __str__(self):
        # return "Trie { key: {}, parent: {}, children: {}, is_terminating: {}".format(key, parent.)