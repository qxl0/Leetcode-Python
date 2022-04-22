"""
392. Is Subsequence
Easy

4652

285

Add to List

Share
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
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
    def isSubsequence(s, t):
        pass


if __name__ == "__main__":
    sol = Solution()
    s = "abc"
    t = "ahbgdc"
    res = sol.isSubsequence(s, t)
    print("Ans is ", res)
