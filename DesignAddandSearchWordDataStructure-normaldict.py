class WordDictionary:
    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        node = self.trie
        for c in word:
            node = node.setdefault(c, {})
        node["$"] = True

    def search(self, word: str) -> bool:
        return self.searchNode(self.trie, word)

    def searchNode(self, node, word: str) -> bool:
        for i, c in enumerate(word):
            if c == ".":
                return any(
                    self.searchNode(node[w], word[i + 1 :]) for w in node if w != "$"
                )
            if c not in node:
                return False
            node = node[c]
        return "$" in node

    # no slicing
    def search(self, word: str) -> bool:
        node = self.root
        self.res = False
        self.dfs(node, word, 0)
        return self.res

    def dfs(self, node, word, i):
        if i >= len(word):
            if node.word:
                self.res = True
            return
        if word[i] == ".":
            for n in node.children.values():
                self.dfs(n, word, i + 1)
        else:
            node = node.children.get(word[i])
            if not node:
                return
            self.dfs(node, word, i + 1)
