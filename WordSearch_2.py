class WordDict:
    def __init__(self):
        self.trie = {}

    def addWord(self, word):
        node = self.trie
        for c in word:
            node = node.setdefault(c, {})  # get the value of key: c,
        node["$"] = True

    def search(self, word):
        node = self.trie
        return self.dfs(node, word)

    def dfs(self, node, word):
        # search to check if node matches word
        for c in word:
            if c not in node:
                return False
            node = node[c]
        return "$" in node


class Solution:
    worddict = WordDict()

    def findWords(self, board, words):
        # set up dict
        for w in words:
            self.worddict.addWord(w)

        # set up dp
        m = len(board)
        n = len(board[0])
        res = []
        for i in range(m):
            for j in range(n):
                self.dfs(board, m, n, i, j, self.worddict.trie, "", res)
        return res

    def dfs(self, board, m, n, i, j, trie, word, res):
        # dfs search board from i j
        if "$" in trie and trie["$"]:
            res.append(word)
            trie["$"] = False
        if i < 0 or i >= m or j < 0 or j >= n:
            return
        if not trie:
            return
        c = board[i][j]
        if c not in trie:
            return
        if c in trie:
            trie = trie[c]
            board[i][j] = "#"
            for x, y in [[-1, 0], [0, -1], [0, 1], [1, 0]]:
                self.dfs(board, m, n, i + x, j + y, trie, word + c, res)
            board[i][j] = c


DIRS = [(-1, 0), (1, 0), (0, 1), (0 - 1)]


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word = None


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = True
        node.word = word

    def search(self, word):
        node = self.root
        for c in word:
            node = node.children.get(c)
        if node is None:
            return None
        return node


class Solution2:
    def wordsearch2(self, board, words):
        if not board or len(board) == 0:
            return []
        trie = Trie()
        for w in words:
            trie.add(w)
        result = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                c = board[i][j]
                self.search(
                    board, i, j, trie.root.children.get(c), set([(i, j)]), result
                )
        return list(result)

    def search(self, board, x, y, node, visited, result):
        if not node:
            return
        if node.is_word:
            result.add(node.word)
        for dx, dy in DIRS:
            x_, y_ = x + dx, y + dy
            if not self.inbounds(board, x_, y_):
                continue
            if (x_, y_) in visited:
                continue
            visited.add((x_, y_))
            self.search(
                board, x_, y_, node.children.get(board[x_][y_]), visited, result
            )
            visited.remove((x_, y_))

    def inbounds(self, board, x, y):
        return 0 <= x < len(board) and 0 <= y < len(board[0])


if __name__ == "__main__":
    sol = Solution()
    board = [
        ["o", "a", "b", "n"],
        ["o", "t", "a", "e"],
        ["a", "h", "k", "r"],
        ["a", "f", "l", "v"],
    ]
    words = ["oa", "oaa"]
    res = sol.findWords(board, words)
    print(res)
