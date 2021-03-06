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
        n = len(s)
        q = [0]
        visited = set()
        visited.add(0)
        while q:
            idx = q.pop(0)
            for i in range(idx + minJump, idx + maxJump + 1):
                if i < n and s[i] == "0":
                    if i == n - 1:
                        return True
                    if i in visited:
                        continue
                    q.append(i)
                    visited.add(i)
        return False


class Solution2:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        if s[n - 1] == "1":
            return False
        numReached = 0
        scanlines = [0] * (n + 1)

        scanlines[0 + minJump] = 1
        scanlines[0 + maxJump + 1] = -1

        for i in range(1, n):
            numReached += scanlines[i]
            if numReached == 0:
                continue
            if s[i] == "1":
                continue

            if i + minJump <= n:
                scanlines[i + minJump] += 1
            if i + maxJump + 1 <= n:
                scanlines[i + maxJump + 1] -= 1

        return numReached > 0


if __name__ == "__main__":
    sol = Solution2()
    s = "011010"
    s = "0110110"
    minJump = 2
    maxJump = 3
    res = sol.canReach(s, minJump, maxJump)
    print("Ans is : ", res)
