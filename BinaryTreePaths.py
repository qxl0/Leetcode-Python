"""
257. Binary Tree Paths
Easy

3986

182

Add to List

Share
Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.
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
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        pass


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode.to_binary_tree([1, 2, 3, None, 5])
    res = sol.binaryTreePaths(root)
    print(res)
