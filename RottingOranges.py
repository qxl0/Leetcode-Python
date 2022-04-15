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
        pass


if __name__ == "__main__":
    s = Solution()
    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]

    res = s.orangesRotting(grid)
    print(res)
