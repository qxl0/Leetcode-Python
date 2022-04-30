"""
1047. Remove All Adjacent Duplicates In String
Easy

3143

153

Add to List

Share
You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

We repeatedly make duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.

 
"""


from curses.ascii import SO
from math import floor
from string import ascii_lowercase
from typing import List


class Solution:
    def removeDuplicates(self, s: str) -> str:
        dup = {ch * 2 for ch in ascii_lowercase}

        l = -1
        while l != len(s):
            l = len(s)
            for d in dup:
                s.replace(d, "")

        return s


if __name__ == "__main__":
    sol = Solution()
    s = "abbaca"
    res = sol.removeDuplicates(s)
    print(res)
