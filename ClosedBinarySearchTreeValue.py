"""
270. Closest Binary Search Tree Value
Easy

1420

86

Add to List

Share
Given the root of a binary search tree and a target value, return the value in the BST that is closest to the target.

 
"""


import collections
import heapq
import random
from typing import List, Optional

from helpers.TreeNode import TreeNode


class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode.to_binary_tree([4, 2, 5, 1, 3])
    res = sol.closestValue(root)
    print("result is: ", res)
