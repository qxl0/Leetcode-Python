"""
1372. Longest ZigZag Path in a Binary Tree
Medium

1111

21

Add to List

Share
You are given the root of a binary tree.

A ZigZag path for a binary tree is defined as follow:

Choose any node in the binary tree and a direction (right or left).
If the current direction is right, move to the right child of the current node; otherwise, move to the left child.
Change the direction from right to left or from left to right.
Repeat the second and third steps until you can't move in the tree.
Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).

Return the longest ZigZag path contained in that tree.
"""


import collections
import heapq
import random
from typing import List, Optional

from helpers.TreeNode import TreeNode


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        longest = 0

        def helper(root):
            if not root:
                return -1, -1
            _, rightLen = helper(root.left)
            leftLen, _ = helper(root.right)
            left = rightLen + 1
            right = leftLen + 1
            longest = max(longest, left, right)
            return left, right

        helper(root)
        return longest


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode.to_binary_tree(
        root=[1, None, 1, 1, 1, None, None, 1, 1, None, 1, None, None, None, 1, None, 1]
    )
    res = sol.longestZigZag(root)
    print("result is: ", res)
