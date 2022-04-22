"""
290. Word Pattern
Easy

3491

403

Add to List

Share
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.
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
    def wordPattern(self, pattern: str, s: str) -> bool:
        pass


if __name__ == "__main__":
    sol = Solution()
    pattern = "abba"
    s = "dog cat cat dog"
    res = sol.wordPattern(pattern, s)
    print(res)
