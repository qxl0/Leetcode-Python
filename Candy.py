# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from random import randint
from typing import List, Optional
from helpers.TreeNode import TreeNode


class Solution:
    def candy(self, ratings: List[int]) -> int:
        def count(n):
            return n * (n + 1) // 2

        n = len(ratings)
        if n <= 1:
            return n
        candies = 0
        up, down = 0, 0
        oldSlope = 0
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                newSlope = 1
            elif ratings[i] < ratings[i - 1]:
                newSlope = -1
            else:
                newSlope = 0
            if oldSlope > 0 and newSlope == 0 or oldSlope < 0 and newSlope >= 0:
                candies += count(up) + count(down) + max(up, down)
                up = 0
                down = 0
            if newSlope > 0:
                up += 1
            elif newSlope < 0:
                down += 1
            else:
                candies += 1
            oldSlope = newSlope
        candies += count(up) + count(down) + max(up, down) + 1
        return candies


if __name__ == "__main__":
    sol = Solution()
    # ratings = [1, 0, 2]
    ratings = [1, 2, 3]
    res = sol.candy(ratings)
    print(res)
