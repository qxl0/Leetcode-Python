class WordNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False


class WordDictionary:
    def __init__(self):
        self.root = WordNode()

    def search(self, word):
        node = self.root
        self.res = False
        self.dfs(node, word, 0)
        return self.res

    def dfs(self, node, word, i):
        if i >= len(word):
            if node.isEnd:
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

    def addWord(self, word):
        node = self.root
        for c in word:
            if c in node.children:
                node = node.children[c]
            else:
                node.children[c] = WordNode()
                node = node.children[c]
        node.isEnd = True


if __name__ == "__main__":
    worddict = WordDictionary()

    worddict.addWord("a")
    worddict.addWord("ab")
    res = worddict.search("..")
    print(res)
