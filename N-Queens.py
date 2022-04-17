"""
51. N-Queens
Hard

5604

152

Add to List

Share
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.
 
"""


import collections
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        pass


if __name__ == "__main__":
    s = Solution()
    n = 4
    res = s.solveNQueens(n)
    print("Ans is:", res)
