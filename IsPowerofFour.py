"""
292. Nim Game
Easy

1049

2202

Add to List

Share
You are playing the following Nim Game with your friend:

Initially, there is a heap of stones on the table.
You and your friend will alternate taking turns, and you go first.
On each turn, the person whose turn it is will remove 1 to 3 stones from the heap.
The one who removes the last stone is the winner.
Given n, the number of stones in the heap, return true if you can win the game assuming both you and your friend play optimally, otherwise return false.
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
    def isPowerOfFour(self, num):
        return num != 0 and num & (num - 1) == 0 and num & 1431655765 == num


if __name__ == "__main__":
    sol = Solution()
    n = 4
    res = sol.isPowerOfFour(n)
    print(res)
