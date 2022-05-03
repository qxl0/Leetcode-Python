"""
1022. Sum of Root To Leaf Binary Numbers
Easy

2504

150

Add to List

Share
You are given the root of a binary tree where each node has a value 0 or 1. Each root-to-leaf path represents a binary number starting with the most significant bit.

For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.
For all leaves in the tree, consider the numbers represented by the path from the root to that leaf. Return the sum of these numbers.

The test cases are generated so that the answer fits in a 32-bits integer.

 
"""


import collections
import heapq
import random
from typing import List, Optional

from helpers.TreeNode import TreeNode


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        sum = 0

        def dfs(node, cur):
            nonlocal sum
            if not node:
                sum += cur
                return
            dfs(node.left, cur * 2 + node.val)
            dfs(node.right, cur * 2 + node.val)

        dfs(root, 0)
        return sum


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode.to_binary_tree([1, 0, 1, 0, 1, 0, 1])
    res = sol.sumRootToLeaf(root)
    print("result is: ", res)
