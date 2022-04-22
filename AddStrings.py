"""
415. Add Strings
Easy

3187

541

Add to List

Share
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.
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
    def addStrings(self, num1: str, num2: str) -> str:
        n1 = list(num1)[::-1]
        n2 = list(num2)[::-1]

        carry = 0
        ret = []
        i1, i2 = 0, 0
        while i1 < len(n1) or i2 < len(n2) or carry:
            sum = 0
            if i1 < len(n1):
                sum += int(n1[i1])
                i1 += 1
            if i2 < len(n2):
                sum += int(n2[i2])
                i2 += 1
            ret.append(str((sum + carry) % 10))
            carry = (sum + carry) // 10
        return "".join(ret[::-1])


if __name__ == "__main__":
    sol = Solution()
    num1 = "11"
    num2 = "123"
    res = sol.addStrings(num1, num2)
    print("Ans is ", res)
