"""
1763. Longest Nice Substring
Easy

580

447

Add to List

Share
A string s is nice if, for every letter of the alphabet that s contains, it appears both in uppercase and lowercase. For example, "abABB" is nice because 'A' and 'a' appear, and 'B' and 'b' appear. However, "abA" is not because 'b' appears, but 'B' does not.

Given a string s, return the longest substring of s that is nice. If there are multiple, return the substring of the earliest occurrence. If there are none, return an empty string.
"""
from typing import List


class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        pass


if __name__ == "__main__":
    sol = Solution()
    s = "YazaAaY"
    res = sol.longestNiceSubstring(s)
    print("result is: ", res)
