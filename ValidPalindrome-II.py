"""
680. Valid Palindrome II
Easy

5541

300

Add to List

Share
Given a string s, return true if the s can be palindrome after deleting at most one character from it.
"""


from math import floor
from typing import List


class Solution:
    def validPalindrome(self, s: str) -> str:
        def isPal(s):
            l, r = 0, len(s) - 1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        l, r = 0, len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return isPal(s[l + 1 : r + 1]) or isPal(s[l:r])
        return True


if __name__ == "__main__":
    sol = Solution()
    # s = "aba"
    s = "cuppucu"
    res = sol.validPalindrome(s)
    print(res)
