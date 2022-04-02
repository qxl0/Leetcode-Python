# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root


if __name__ == "__main__":
    sol = Solution()
    p = TreeNode(4)
    p.left = TreeNode(2)
    p.right = TreeNode(7)
    p.left.left = TreeNode(1)
    p.left.right = TreeNode(3)
    p.right.left = TreeNode(6)
    p.right.right = TreeNode(9)
    res = sol.invertTree(p)
    print(res)
