"""
110. Balanced Binary Tree
Easy

5516

298

Add to List

Share
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
"""


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [True, 0]
            l = dfs(root.left)
            r = dfs(root.right)
            balanced = abs(l[1] - r[1]) <= 1 and l[0] and r[0]
            return [balanced, max(l[1], r[1]) + 1]

        return dfs(root)[0]


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(10)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(7)
    res = sol.isBalanced(root)
    print(res)
