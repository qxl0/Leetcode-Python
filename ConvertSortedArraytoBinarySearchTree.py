"""
108. Convert Sorted Array to Binary Search Tree
Easy

6197

349

Add to List

Share
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.
"""


from typing import List, Optional
from helpers.TreeNode import TreeNode


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """
        Do not return anything, modify nums in-place instead.
        """


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(0)
    root.left = TreeNode(-3)
    root.leftleft = TreeNode(10)
    root.right = TreeNode(9)
    root.right.left = TreeNode(5)
    res = sol.levelOrderBottom(root)
    print(res)
