"""
263. Ugly Number
Easy

1386

1020

Add to List

Share
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return true if n is an ugly number.
"""


import collections
from typing import List, Optional
from helpers.TreeNode import TreeNode


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 0:
            return False
        for p in (2, 3, 5):
            while n % p == 0:
                n = n // p

        return n == 1


if __name__ == "__main__":
    sol = Solution()
    n = 6
    res = sol.isUgly(n)
    print(res)
