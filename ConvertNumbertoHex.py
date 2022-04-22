"""
405. Convert a Number to Hexadecimal
Easy

866

169

Add to List

Share
Given an integer num, return a string representing its hexadecimal representation. For negative integers, two’s complement method is used.

All the letters in the answer string should be lowercase characters, and there should not be any leading zeros in the answer except for the zero itself.

Note: You are not allowed to use any built-in library method to directly solve this problem.
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
    def toHex(self, num: int) -> str:
        mapping = {i: str(i) for i in range(10)} | {
            10: "a",
            11: "b",
            12: "c",
            13: "d",
            14: "e",
            15: "f",
        }

        if num < 0:
            num += 2**32
        ret = []
        while num:
            lastdigit = mapping[num % 16]
            ret.append(lastdigit)
            num //= 16
        return "".join(ret[::-1])


if __name__ == "__main__":
    sol = Solution()
    num = 26
    res = sol.toHex(num)
    print("Ans is ", res)
