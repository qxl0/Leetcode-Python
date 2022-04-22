"""
367. Valid Perfect Square
Easy

2188

232

Add to List

Share
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Follow up: Do not use any built-in library function such as sqrt.
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
    def isPerfectSquare(self, num):
        l, r = 1, num
        while l <= r:
            print(f"{l} - {r}")
            mid = l + (r - l) // 2
            if mid * mid == num:
                return True
            elif mid * mid > num:
                r = mid - 1
            else:
                l = mid + 1
        return False


if __name__ == "__main__":
    sol = Solution()
    num = 100
    res = sol.isPerfectSquare(num)
    print(res)
