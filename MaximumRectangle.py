"""
85. Maximal Rectangle
Hard

6481

106

Add to List

Share
Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.
"""


from typing import List, Optional
from helpers.LinkedList import Node


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        """
        Do not return anything, modify nums in-place instead.
        """


if __name__ == "__main__":
    sol = Solution()
    matrix = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"],
    ]
    res = sol.maximalRectangle(matrix)
    print(res)
