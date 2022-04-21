"""
99. Recover Binary Search Tree
Medium

5173

176

Add to List

Share
You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.
"""


import sys
from typing import List, Optional
from helpers.TreeNode import TreeNode


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def inorder(node):
            nonlocal first, second, prev
            if not node:
                return
            inorder(node.left)
            if not first and prev.val >= node.val:
                first = prev
                # print("found first: ", first.val if first else "null")
            if first and prev.val >= node.val:
                second = node
                # print("found second: ", second.val if second else "null")
            # print("set prev: ", node.val if node else "null")
            prev = node
            inorder(node.right)

        first, second, prev = None, None, TreeNode(-sys.maxsize / 2)
        inorder(root)
        first.val, second.val = second.val, first.val


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode.to_binary_tree([3, 1, 4, None, None, 2])
    res = sol.recoverTree(root)
    print(res)
