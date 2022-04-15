from collections import deque
import math

from typing import List

"""
994. Rotting Oranges
Medium

6351

272

Add to List

Share
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
"""


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        visit, curr = set(), deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    visit.add((i, j))
                elif grid[i][j] == 2:
                    curr.append((i, j))
        result = 0
        while visit and curr:
            for _ in range(len(curr)):
                i, j = curr.popleft()
                for coord in ((i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)):
                    if coord in visit:
                        visit.remove(coord)
                        curr.append(coord)
            result += 1
        return result if not visit else -1


if __name__ == "__main__":
    s = Solution()
    grid = [[2, 1, 1], [1, 1, 0], [0, 0, 1]]

    res = s.orangesRotting(grid)
    print(res)
