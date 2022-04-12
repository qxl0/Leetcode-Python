"""
Is Valid BST
"""


import sys
from typing import List, Optional
from helpers.TreeNode import TreeNode


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inorder(node):
            if not node:
                return None
            left = inorder(node.left)
            right = inorder(node.right)
            return left + node.val + right


if __name__ == "__main__":
    sol = Solution()
    s = [5, 4, 6, None, None, 3, 7]
    root = TreeNode.to_binary_tree(s)
    res = sol.isValidBST(root)
    print("Ans is: ", res)
