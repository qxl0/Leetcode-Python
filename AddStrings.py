"""
415. Add Strings
Easy

3187

541

Add to List

Share
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.
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
    def addStrings(self, num1: str, num2: str) -> str:
        pass


if __name__ == "__main__":
    sol = Solution()
    num1 = "11"
    num2 = "123"
    res = sol.addStrings(num1, num2)
    print("Ans is ", res)
