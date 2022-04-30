"""
696. Count Binary Substrings
Easy

2842

603

Add to List

Share
Give a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.

 
"""


from math import floor
from typing import List


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        s = map(len, s.replace("01", "0 1").replace("10", "1 0").split())
        s = list(s)
        print(s)
        return sum(min(a, b) for a, b in zip(s, s[1:]))


class Solution2:
    def countBinarySubstrings(self, s: str) -> int:
        ans = 0
        cur = 1
        pre = 0
        for i in range(1, len(s)):
            if s[i - 1] != s[i]:
                ans += min(pre, cur)
                pre, cur = cur, 1
            else:
                cur += 1
        return ans


if __name__ == "__main__":
    sol = Solution2()
    s = "00110011"
    res = sol.countBinarySubstrings(s)
    print(res)
