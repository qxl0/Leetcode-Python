"""
383. Ransom Note
Easy

1661

302

Add to List

Share
Given two strings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.
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
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = collections.Counter(magazine)

        for c in ransomNote:
            if c not in counter:
                return False
            counter[c] -= 1
            if counter[c] < 0:
                return False
        return True


if __name__ == "__main__":
    sol = Solution()
    ransomNote = "a"
    magazine = "b"
    res = sol.canConstruct(ransomNote, magazine)
    print("Ans is ", res)
