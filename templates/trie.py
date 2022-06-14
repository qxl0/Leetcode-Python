class Trie:
    def __init__(self):
        self.children = {}
        self.isword = False

    @staticmethod
    def create(words):
        root = Trie()
        for w in words:
            node = root
            for c in w:
                node.children.setdefault(c, Trie())
                node = node.children
            node.isword = True
        return root
