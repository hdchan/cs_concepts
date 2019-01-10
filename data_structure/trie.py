from .trie_node import TrieNode as Node

class Trie(object):

    def __init__(self):
        self.root = Node()

    def insert(self, collection):
        current = self.root

        for value in collection:
            if value not in current.children:
                current.children[value] = Node(value, current)
            
            current = current.children[value]

        current.is_terminating = True

    def contains(self, collection):
        current = self.root

        for value in collection:
            if value not in current.children:
                return False
            current = current.children[value]
        
        return current.is_terminating

    def remove(self, collection):
        current = self.root

        for value in collection:
            if value not in current.children:
                return -1
            current = current.children[value]
            # print("Traversing to: {}".format(current.key))

        if current.is_terminating == False:
            return -1 # it's not a valid word
        
        current.is_terminating = False

        while current.parent != None and not current.children and current.is_terminating == False:
            # print("Removing: {} with children {}".format(current.key, current.children))
            parent = current.parent
            parent.children.pop(current.key, None)
            current = parent
            # print(current.parent, current.children, current.is_terminating)

        return 0

    def collections(self, collection_prefix):
        current = self.root

        for value in collection_prefix:
            if value not in current.children:
                return []
            current = current.children[value]
        
        return self._collections(collection_prefix, current)

    def _collections(self, starting_prefix, after_node):

        results = []

        if after_node.is_terminating:
            results.append(starting_prefix)
        
        for child in after_node.children.values():
            prefix = starting_prefix[:]
            prefix.append(child.key)
            results += self._collections(prefix, child)
        
        results = ["".join(x) for x in results]
        
        return results