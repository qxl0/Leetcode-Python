"""
99. Recover Binary Search Tree
Medium

5173

176

Add to List

Share
You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.
"""


from typing import List, Optional
from helpers.TreeNode import TreeNode


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.left.right = TreeNode(2)
    res = sol.recoverTree(root)
    print(res)
