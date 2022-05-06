"""
2174. Remove All Ones With Row and Column Flips II
Medium

38

2

Add to List

Share
You are given a 0-indexed m x n binary matrix grid.

In one operation, you can choose any i and j that meet the following conditions:

0 <= i < m
0 <= j < n
grid[i][j] == 1
and change the values of all cells in row i and column j to zero.

Return the minimum number of operations needed to remove all 1's from grid.
 
"""


import collections
from typing import List


class Solution:
    def removeOnes(self, grid: List[List[int]]) -> int:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(grid), len(grid[0])
        seen = set()
        self.res = float("inf")

        def helper(total):
            pos = [
                (i, j)
                for i in range(m)
                for j in range(n)
                if grid[i][j] == 1 and ("r", i) not in seen and ("c", j) not in seen
            ]
            if not pos:
                self.res = min(self.res, total)
            for i, j in pos:
                seen.add(("r", i))
                seen.add(("c", j))
                helper(total + 1)
                seen.remove(("r", i))
                seen.remove(("c", j))

        helper(0)
        return self.res


if __name__ == "__main__":
    sol = Solution()
    grid = [[1, 1, 1], [1, 1, 1], [0, 1, 0]]
    res = sol.removeOnes(grid)
    print("Ans is:", res)
