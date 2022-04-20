"""
87. Scramble String
Hard

1413

928

Add to List

Share
We can scramble a string s to get a string t using the following algorithm:

If the length of the string is 1, stop.
If the length of the string is > 1, do the following:
Split the string into two non-empty substrings at a random index, i.e., if the string is s, divide it to x and y where s = x + y.
Randomly decide to swap the two substrings or to keep them in the same order. i.e., after this step, s may become s = x + y or s = y + x.
Apply step 1 recursively on each of the two substrings x and y.
Given two strings s1 and s2 of the same length, return true if s2 is a scrambled string of s1, otherwise, return false.
"""


from typing import List, Optional
from helpers.LinkedList import Node


class Solution:
    dict = {}

    def isScramble(self, s1: str, s2: str) -> bool:
        """
        Do not return anything, modify nums in-place instead.
        """
        if (s1, s2) in self.dict:
            return self.dict[(s1, s2)]
        n, m = len(s1), len(s2)
        if n != m or sorted(s1) != sorted(s2):
            self.dict[(s1, s2)] = False
            return False
        if n < 4 or s1 == s2:
            self.dict[(s1, s2)] = True
            return True
        f = self.isScramble
        for i in range(1, len(s1)):
            if (
                f(s1[:i], s2[:i])
                and f(s1[i:], s2[i:])
                or f(s1[:i], s2[-i:])
                and f(s1[i:], s2[:-i])
            ):
                self.dict[(s1, s2)] = True
                return True
        self.dict[(s1, s2)] = False
        return False


if __name__ == "__main__":
    sol = Solution()
    # s1 = "great"
    # s2 = "rgeat"
    s1 = "eebaacbcbcadaaedceaaacadccd"
    s2 = "eadcaacabaddaceacbceaabeccd"
    res = sol.isScramble(s1, s2)
    print(res)
