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
        if len(s) < 2:
            return ""

        hs = set(s)
        badchars = {ch for ch in hs if ch.swapcase() not in hs}

        if len(badchars) == 0:
            return s
        if len(hs) == len(badchars):
            return ""

        substrs = []
        lp = 0
        for i in range(len(s)):
            if s[i] in badchars:
                if lp != i:
                    substrs.append(s[lp:i])
                lp = i + 1
        substrs.append(s[lp:])

        return sorted(
            [self.longestNiceSubstring(x) for x in substrs], key=len, reverse=True
        )[0]


if __name__ == "__main__":
    sol = Solution()
    s = "YazaAaY"
    res = sol.longestNiceSubstring(s)
    print("result is: ", res)
