"""
102. Binary Tree Level Order Traversal
Medium

7841

154

Add to List

Share
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
"""


from typing import Optional
from helpers.TreeNode import TreeNode


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        pass


if __name__ == "__main__":
    sol = Solution()
    s = [3, 9, 20, None, None, 15, 7]
    root = TreeNode.to_binary_tree(s)
    res = sol.levelOrder(root)
    print("Ans is: ", res)
