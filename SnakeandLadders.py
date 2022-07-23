from collections import Counter
import heapq
from math import inf
from re import I
from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        q = [1]
        need = {1: 0}
        while q:
            x = q.pop(0)
            for i in range(x + 1, x + 7):
                a, b = (i - 1) // n, (i - 1) % n
                val = board[~a][b if a % 2 == 0 else ~b]
                if val > 0:
                    i = val
                if i == n * n:
                    return need[x] + 1
                if i not in need:
                    need[i] = need[x] + 1
                    q.append(i)
        return -1


if __name__ == "__main__":
    sol = Solution()
    board = [[1, 1, -1], [1, 1, 1], [-1, 1, 1]]
    res = sol.snakesAndLadders(board)
    print(res)
