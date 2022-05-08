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
        pass


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode.to_binary_tree([2, 1, 4, None, None, 3])
    res = sol.increasingBST(root)
    print("Ans is: ", res)
