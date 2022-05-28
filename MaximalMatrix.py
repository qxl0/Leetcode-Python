"""

"""

import collections
from math import floor
from typing import List, Optional
from helpers.TreeNode import TreeNode


class Solution:
    def maximalSquare(self, matrix):
        pass


if __name__ == "__main__":
    sol = Solution()
    matrix = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"],
    ]
    res = sol.maximalSquare(matrix)
    print("Ans is: ", res)
