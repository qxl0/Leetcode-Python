"""
434. Number of Segments in a String
Easy

435

1008

Add to List

Share
Given a string s, return the number of segments in the string.

A segment is defined to be a contiguous sequence of non-space characters.
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
    def countSegments(self, s: str) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    s = "Hello, my name is John"
    res = sol.countSegments(s)
    print("Ans is ", res)
