"""
159. Longest Substring with At Most Two Distinct Characters
Medium

1685

25

Add to List

Share
Given a string s, return the length of the longest substring that contains at most two distinct characters.
"""


from typing import List, Optional
from helpers.LinkedList import LinkedList
from helpers.LinkedList import ListNode
from helpers.TreeNode import TreeNode


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        """
        Do not return anything, modify nums in-place instead.
        """
        d = {}
        longest = 1
        start = 0
        for i, c in enumerate(s):
            d[c] = d.get(c, 0) + 1
            while len(d) > 2:
                d[s[start]] -= 1
                if d[s[start]] == 0:
                    d.pop(s[start])
                start += 1
            longest = max(longest, i - start + 1)

        return longest


if __name__ == "__main__":
    sol = Solution()
    # s = "eceba"
    # s = "ccaabbb"
    s = "abaccc"
    res = sol.lengthOfLongestSubstringTwoDistinct(s)
    print(res)
