"""
298. Binary Tree Longest Consecutive Sequence
Medium

891

212

Add to List

Share
Given the root of a binary tree, return the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path needs to be from parent to child (cannot be the reverse).
"""

from math import inf
from this import d
from typing import List, Optional

from helpers.TreeNode import TreeNode


class Solution:
    def __init__(self):
        self.longest = 0

    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            if not root:
                return 0
            left = helper(root.left)
            right = helper(root.right)
            length = 1
            if root.left and root.left.val == root.val + 1:
                length = max(length, left + 1)
            if root.right and root.right.val == root.val + 1:
                length = max(length, right + 1)
            self.longest = max(self.longest, length)
            print(self.longest)
            return length

        helper(root)
        return self.longest


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode.to_binary_tree([1, None, 3, 2, 4, None, None, None, 5])
    res = sol.longestConsecutive(root)
    print(res)
