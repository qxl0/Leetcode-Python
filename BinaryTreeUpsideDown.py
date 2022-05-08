"""
156. Binary Tree Upside Down
Medium

129

221

Add to List

Share
Given the root of a binary tree, turn the tree upside down and return the new root.

You can turn a binary tree upside down with the following steps:

The original left child becomes the new root.
The original root becomes the new right child.
The original right child becomes the new left child.
"""

import collections
from math import floor
from typing import List, Optional
from helpers.TreeNode import TreeNode


class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(node):
            if not node or not node.left:
                return node
            newRoot = helper(node.left)
            node.left.left = node.right
            node.left.right = node
            node.left = node.right = None
            return newRoot

        return helper(root)


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode.to_binary_tree([1, 2, 3, 6, 7])
    res = sol.upsideDownBinaryTree(root)
    print("Ans is: ", res)
