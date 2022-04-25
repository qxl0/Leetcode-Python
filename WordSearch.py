from operator import truediv

"""
79. Word Search
Medium

8829

337

Add to List

Share
Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are 
horizontally or vertically neighboring. The same letter cell may not be used more than once.
"""


class Solution:
    def helper(self, board, word, i, j):
        if len(word) == 0:
            return True
        if i < 0 or i >= len(board) or j >= len(board[0]) or word[0] != board[i][j]:
            return False
        originalChar = board[i][j]
        board[i][j] = "#"
        res = (
            self.helper(board, word[1:], i + 1, j)
            or self.helper(board, word[1:], i - 1, j)
            or self.helper(board, word[1:], i, j - 1)
            or self.helper(board, word[1:], i, j + 1)
        )
        board[i][j] = originalChar
        return res

    def exists(self, board, word):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.helper(board, word, i, j):
                    return True


class Solution2:
    directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

    def wordsearch(self, board, word):
        if not word:
            return False
        self.m, self.n = len(board), len(board[0])
        for i in range(self.m):
            for j in range(self.n):
                if self.dfs(board, i, j, word):
                    return True
        return False

    def dfs(self, board, i, j, w):
        if len(w) == 0:
            return True
        if i < 0 or i >= self.m or j < 0 or j >= self.n or board[i][j] != w[0]:
            return False
        original = board[i][j]
        res = False
        board[i][j] = "#"
        for di, dj in self.directions:
            res = res or self.dfs(board, i + di, j + dj, w[1:])
            if res:
                return True
        # res = (
        #     self.dfs(board, i + 1, j, w[1:])
        #     or self.dfs(board, i - 1, j, w[1:])
        #     or self.dfs(board, i, j - 1, w[1:])
        #     or self.dfs(board, i, j + 1, w[1:])
        # )

        board[i][j] = original
        return res


if __name__ == "__main__":
    # board = [["a", "b", "c", "e"], ["d", "e", "c", "s"], ["a", "a", "e", "e"]]
    # word = "abcced"
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "SEE"
    s = Solution2()
    res = s.wordsearch(board, word)
    print("Word exists: ", res)
