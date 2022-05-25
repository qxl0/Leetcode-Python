# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional
from helpers.TreeNode import TreeNode


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        if not matrix:
            return False

        def helper(target, left, right, up, down):
            if left > right or up > down:
                return False
            if matrix[up][left] > target or matrix[down][right] < target:
                return False
            row = up
            while row < down:
                mid = (left + right) // 2
                if matrix[row][mid] == target:
                    return True

                row += 1
            return helper(target, left, mid - 1, row, down) or helper(
                target, mid + 1, right, up, row - 1
            )

        return helper(target, 0, n - 1, 0, m - 1)


if __name__ == "__main__":
    sol = Solution()
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30],
    ]
    res = sol.searchMatrix(matrix)
    print(res)
