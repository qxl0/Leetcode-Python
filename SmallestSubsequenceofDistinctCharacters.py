"""
1081. Smallest Subsequence of Distinct Characters
Medium

1627

143

Add to List

Share
Given a string s, return the lexicographically smallest subsequence of s that contains all the distinct characters of s exactly once.
"""
from collections import defaultdict
import collections
from math import factorial
from operator import itemgetter
from typing import List


class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last = {c: i for i, c in enumerate(s)}
        stack = []
        for i, c in enumerate(s):
            if c in stack:
                continue
            while stack and stack[-1] > c and i < last[stack[-1]]:
                stack.pop()
            stack.append(c)
        return "".join(stack)


if __name__ == "__main__":
    sol = Solution()
    s = "bcabc"
    res = sol.smallestSubsequence(s)
    print(res)
