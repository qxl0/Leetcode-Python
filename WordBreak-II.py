"""
140. Word Break II
Hard

4620

476

Add to List

Share
Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.
"""


from typing import List, Optional
from helpers.TreeNode import TreeNode


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        pass


if __name__ == "__main__":
    sol = Solution()
    s = "catsanddog"
    wordDict = ["cat", "cats", "and", "sand", "dog"]
    res = sol.wordBreak(s, wordDict)
    print(res)
