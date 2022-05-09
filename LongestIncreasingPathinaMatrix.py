"""
329. Longest Increasing Path in a Matrix
Hard

5265

90

Add to List

Share
Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).
"""


import collections
import heapq
import random
from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo = {}
        dt = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def helper(i, j, memo):
            if (i, j) in memo:
                return memo[(i, j)]
            for dx, dy in dt:
                newi, newj = i + dx, j + dy
                length = 0
                if (
                    newi >= 0
                    and newi < m
                    and newj >= 0
                    and newj < n
                    and matrix[newi][newj] > matrix[i][j]
                ):
                    length = max(length, helper(newi, newj, memo))
            memo[(i, j)] = length + 1
            return memo[(i, j)]

        m, n = len(matrix), len(matrix[0])
        longest = 1
        for i in range(m):
            for j in range(n):
                longest = max(longest, helper(i, j, memo))
        return longest


if __name__ == "__main__":
    sol = Solution()
    matrix = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]
    res = sol.longestIncreasingPath(matrix)
    print("result is: ", res)
