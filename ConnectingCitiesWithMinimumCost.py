"""
1135. Connecting Cities with Minimum Cost
"""


import sys
from typing import List, Optional
from helpers.TreeNode import TreeNode


class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    N = 3
    connections = [[1, 2, 5], [1, 3, 6], [2, 3, 1]]
    res = sol.minimumCost(N, connections)
    print("Ans is: ", res)
