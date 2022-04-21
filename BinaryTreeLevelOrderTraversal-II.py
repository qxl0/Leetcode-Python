"""
107. Binary Tree Level Order Traversal II
Medium

3131

275

Add to List

Share
Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values. (i.e., from left to right, level by level from leaf to root).
"""


from typing import List, Optional
from helpers.TreeNode import TreeNode


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Do not return anything, modify nums in-place instead.
        """
        ans = []

        def traverse(node, level):
            nonlocal ans
            if not node:
                return
            if level > len(ans):
                ans.append([node.val])
            else:
                ans[level - 1].extend([node.val])
            traverse(node.left, level + 1)
            traverse(node.right, level + 1)

        traverse(root, 1)
        return ans[::-1]


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    res = sol.levelOrderBottom(root)
    print(res)
