"""
1044. Longest Duplicate Substring
Hard

1619

318

Add to List

Share
Given a string s, consider all duplicated substrings: (contiguous) substrings of s that occur 2 or more times. The occurrences may overlap.

Return any duplicated substring that has the longest possible length. If s does not have a duplicated substring, the answer is "".
"""
from math import factorial
from typing import List


class Solution:
    def longestDupSubstring(self, s: str) -> str:
        pass


if __name__ == "__main__":
    sol = Solution()
    s = "banana"
    res = sol.longestDupSubstring(s)
    print(res)
