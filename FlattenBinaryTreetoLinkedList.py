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


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode.to_binary_tree([1, 2, 5, 3, 4, None, 6])
    res = sol.flatten(root)
    print(res)
