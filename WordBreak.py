"""
LeetCode 139. Word Break
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.
"""


from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        ok = [True]
        for i in range(1, len(s) + 1):
            ok += (any(ok[j] and s[j:i] in wordDict for j in range(i)),)
        return ok[-1]

    def wordBreak2(self, s: str, wordDict: List[str]) -> bool:
        ok = [True]
        for i in range(1, len(s) + 1):
            isok = False
            for j in range(i):
                if ok[j] and s[j:i] in wordDict:
                    isok = True
                    break
            ok.append(isok)
        return ok[-1]

    def wordBreak(self, s, words):
        ok = [True]
        max_len = max(map(len, words + [""]))
        words = set(words)
        for i in range(1, len(s) + 1):
            ok += (
                any(ok[j] and s[j:i] in words for j in range(max(0, i - max_len), i)),
            )
        return ok[-1]


if __name__ == "__main__":
    sol = Solution()
    s = "leetcode"
    wordDict = ["leet", "code"]
    # res = sol.wordBreak(s, wordDict)
    res2 = sol.wordBreak2(s, wordDict)
    print(res2)
