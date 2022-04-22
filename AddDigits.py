"""
258. Add Digits
Easy

2416

1644

Add to List

Share
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.
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
    def addDigits(self, num: int) -> int:
        def addnumdigits(num):
            sum = 0
            while num:
                sum += num % 10
                num //= 10
            return sum

        while num // 10:
            num = addnumdigits(num)
        return num


if __name__ == "__main__":
    sol = Solution()
    num = 38
    res = sol.addDigits(num)
    print(res)
