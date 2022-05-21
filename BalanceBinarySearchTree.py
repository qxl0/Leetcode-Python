"""
1382. Balance a Binary Search Tree
Medium

1857

57

Add to List

Share
Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.

A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.
"""


from math import floor
from tkinter.tix import Tree
from typing import List

from helpers.TreeNode import TreeNode


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        inorder = []

        def helper(node):
            if not node:
                return
            helper(node.left)
            inorder.append(node.val)
            helper(node.right)

        helper(root)

        # construct based on inorder
        def constructBST(left, right):
            print(left, right)
            if left > right:
                return None
            mid = left + (right + left) // 2
            cur = TreeNode(inorder[mid])
            cur.left = constructBST(left, mid - 1)
            cur.right = constructBST(mid + 1, right)
            return cur

        helper(root)
        return constructBST(0, len(inorder) - 1)


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    root.right.right.right = TreeNode(4)
    res = sol.balanceBST(root)

    print(res)
