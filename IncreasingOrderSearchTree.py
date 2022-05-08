"""
897. Increasing Order Search Tree
Easy

3201

629

Add to List

Share
Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.
"""

import collections
from math import floor
from typing import List
from helpers.TreeNode import TreeNode


class Solution:
    def increasingBST(self, root):
        dummy = pre = TreeNode()

        def helper(node):
            nonlocal pre
            if not node:
                return None
            helper(node.left)
            node.left = None
            pre.right = node
            pre = pre.right
            helper(node.right)

        helper(root)
        return dummy.right


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode.to_binary_tree([2, 1, 4, None, None, 3])
    res = sol.increasingBST(root)
    print("Ans is: ", res)
