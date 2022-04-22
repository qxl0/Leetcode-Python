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
        d = {}
        r = {}
        wordlist = s.split(" ")
        if len(wordlist) != len(pattern):
            return False
        for p, w in zip(pattern, wordlist):
            if p not in d and w not in r:
                d[p] = w
                r[w] = p
            else:
                if p in d and w != d[p]:
                    return False
                if w in r and r[w] != p:
                    return False
        return True


if __name__ == "__main__":
    sol = Solution()
    pattern = "abba"
    s = "dog dog dog dog"
    res = sol.wordPattern(pattern, s)
    print(res)
