"""
409. Longest Palindrome
Easy

2609

154

Add to List

Share
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.
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
    def longestPalindrome(self, s: str) -> int:
        counter = collections.Counter(s)
        ans = 0
        flag = 0
        for c in counter:
          if counter[c] % 2 == 0:
            ans += counter[c]
          else:
            ans += counter[c] -1
            flag = 1
        return ans if flag == 0 else ans+1



if __name__ == "__main__":
    sol = Solution()
    s = "abccccdd"
    res = sol.longestPalindrome(s)
    print("Ans is ", res)
