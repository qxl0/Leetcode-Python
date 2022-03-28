from operator import truediv
from typing import List

"""
Word Search 2
Description
Given a matrix of lower alphabets and a dictionary. Find all words in the dictionary that can be found in the matrix. A word can start from any position in 
the matrix and go left/right/up/down to the adjacent position. One character only be used once in one word. No same word in dictionary
"""


class Solution:
    def word_search_i_i(self, board: List[List[str]], words: List[str]) -> List[str]:
        DIRS = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def helper(board, i, j, w):
            if len(w) == 0:
                return True
            if (
                i < 0
                or i >= len(board)
                or j < 0
                or j >= len(board[0])
                or board[i][j] != w[0]
            ):
                return False
            if visited[i][j]:
                return False

            visited[i][j] = True
            for dx, dy in DIRS:
                xx, yy = i + dx, j + dy
                if helper(board, xx, yy, w[1:]):
                    return True
            visited[i][j] = False
            return False

        res = []
        for word in words:
            visited = [[False for j in range(len(board[0]))] for j in range(len(board))]
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if helper(board, i, j, word):
                        res.append(word)
        return res


if __name__ == "__main__":
    board = ["doaf", "agai", "dcan"]
    words = ["dog", "dad", "dgdg", "can", "again"]
    s = Solution()
    res = s.word_search_i_i(board, words)
    print("word list: ", res)
