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
