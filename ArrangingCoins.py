"""
441. Arranging Coins
Easy

2161

1013

Add to List

Share
You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

Given the integer n, return the number of complete rows of the staircase you will build.
"""
import collections
from typing import List, Optional
from helpers.TreeNode import TreeNode


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def arrangeCoins(self, n: int) -> int:
        def checkOK(m):
            t = m * (m + 1) // 2
            if t <= n:
                return True
            return False

        l, r = 1, n

        while l < r:
            mid = r - (r - l) // 2
            print(f"l={l},r={r} ===> m={mid}")
            if checkOK(mid):
                l = mid
            else:
                r = mid - 1
        return l


if __name__ == "__main__":
    sol = Solution()
    n = 5
    res = sol.arrangeCoins(n)
    print("Ans is ", res)
