"""
1871. Jump Game VII
Medium

850

50

Add to List

Share
You are given a 0-indexed binary string s and two integers minJump and maxJump. In the beginning, you are standing at index 0, which is equal to '0'. You can move from index i to index j if the following conditions are fulfilled:

i + minJump <= j <= min(i + maxJump, s.length - 1), and
s[j] == '0'.
Return true if you can reach index s.length - 1 in s, or false otherwise.
"""
import collections
import sys
from typing import List


class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        pass


if __name__ == "__main__":
    sol = Solution()
    s = "011010"
    minJump = 2
    maxJump = 3
    res = sol.canReach(s, minJump, maxJump)
    print("Ans is : ", res)
