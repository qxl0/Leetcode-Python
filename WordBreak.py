"""
LeetCode 139. Word Break
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.
"""


from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        pass


if __name__ == "__main__":
    sol = Solution()
    s = "leetcode"
    wordDict = ["leet", "code"]
    res = sol.wordBreak(s, wordDict)
    print(res)
