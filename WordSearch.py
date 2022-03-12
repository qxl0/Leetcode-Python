from operator import truediv


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


if __name__ == "__main__":
    board = [["a", "b", "c", "e"], ["s", "f", "c", "s"], ["a", "d", "e", "e"]]
    word = "abcced"
    s = Solution()
    res = s.exists(board, word)
    print("Word exists: ", res)
