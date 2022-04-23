"""
114. Flatten Binary Tree to Linked List
Medium

6930

464

Add to List

Share
Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.
"""


from typing import List, Optional
from helpers.TreeNode import TreeNode


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        dummy = TreeNode(0)
        dummy.right = root

        def dfs(node, ret):
            if not node:
                return node
            ret.append(node)
            if node.left:
                dfs(node.left, ret)
            if node.right:
                dfs(node.right, ret)

        ret = []
        dfs(root, ret)
        for i in range(len(ret)):
            ret[i].left = None
            if i < len(ret) - 1:
                ret[i].right = ret[i + 1]
        return dummy.right


class Solution2:
    def __init__(self):
        self.prev = None

    def flatten(self, root):
        if not root:
            return None
        self.flatten(root.right)
        self.flatten(root.left)

        root.right = self.prev
        root.left = None
        self.prev = root


if __name__ == "__main__":
    sol = Solution2()
    # root = TreeNode.to_binary_tree([1, 2, 5, 3, 4, None, 6])
    root = TreeNode.to_binary_tree([1, 3, 4])
    res = sol.flatten(root)
    print(res)
