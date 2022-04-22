"""
404. Sum of Left Leaves
Easy

3264

244

Add to List

Share
Given the root of a binary tree, return the sum of all left leaves.

A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.
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
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode.to_binary_tree([3, 9, 20, None, None, 15, 7])
    res = sol.sumOfLeftLeaves(root)
    print("Ans is ", res)
