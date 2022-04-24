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
        ret = []
        dict = set(wordDict)

        def helper(s, path):
            if len(s) == 0:
                ret.append(" ".join(path))
                return
            for i in range(1, 1 + len(s)):
                if s[:i] in dict:
                    helper(s[i:], path + [s[:i]])

        helper(s, [])
        return ret


if __name__ == "__main__":
    sol = Solution()
    s = "catsanddog"
    wordDict = ["cat", "cats", "and", "sand", "dog"]
    res = sol.wordBreak(s, wordDict)
    print(res)
