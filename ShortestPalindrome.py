"""

"""

import collections
from math import floor
from typing import List, Optional
from helpers.TreeNode import TreeNode


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        t = "#"
        for i in range(len(s)):
            t += s[i]
            t += "#"
        n = len(t)
        P = [0] * n
        L = 0
        maxCenter, maxRight = -1, -1
        for i in range(n):
            r = 0
            print("work on:", i, "maxRight: ", maxRight)
            if i < maxRight:
                j = maxCenter * 2 - i
                r = min(P[j], maxRight - i)
                print(i, ": initial set to ", r)
            while i - r >= 0 and i + r < n and t[i - r] == t[i + r]:
                r += 1
            P[i] = r - 1
            if i + P[i] > maxRight:
                maxRight = i + P[i]
                maxCenter = i
                # print(maxCenter,maxRight)
            if i - P[i] == 0:
                L = (P[i] * 2 + 1) // 2  # -->s
        return s[L:][::-1] + s


if __name__ == "__main__":
    sol = Solution()
    s = "aabba"
    res = sol.shortestPalindrome(s)
    print("Ans is: ", res)
