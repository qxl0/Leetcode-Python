"""
345. Reverse Vowels of a String
Easy

1574

1829

Add to List

Share
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.
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
    def reverseVowels(self, s: str) -> str:
        pass


if __name__ == "__main__":
    sol = Solution()
    s = "hello"
    res = sol.reverseVowels(s)
    print("Ans is ", res)
