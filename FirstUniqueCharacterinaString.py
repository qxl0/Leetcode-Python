"""
387. First Unique Character in a String
Easy

4864

194

Add to List

Share
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
"""


import collections
from typing import List, Optional
from helpers.TreeNode import TreeNode


class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = collections.Counter(s)
        for i, c in enumerate(s):
            if counter[c] == 1:
                return i
        return -1


if __name__ == "__main__":
    sol = Solution()
    s = "leetcode"
    res = sol.firstUniqChar(s)
    print(res)
