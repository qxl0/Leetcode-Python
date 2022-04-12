"""
Is Valid BST
"""


import sys
from typing import List, Optional
from helpers.TreeNode import TreeNode


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inorder(node, output):
            if not node:
                return
            inorder(node.left, output)
            output.append(node.val)
            inorder(node.right, output)

        output = []
        inorder(root, output)
        for i in range(1, len(output)):
            if output[i] <= output[i - 1]:
                return False
        return True


if __name__ == "__main__":
    sol = Solution()
    s = [5, 4, 6, None, None, 3, 7]
    root = TreeNode.to_binary_tree(s)
    res = sol.isValidBST(root)
    print("Ans is: ", res)
