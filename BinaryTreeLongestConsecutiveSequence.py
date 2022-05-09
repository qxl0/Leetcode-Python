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
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode.to_binary_tree([1, None, 3, 2, 4, None, None, None, 5])
    res = sol.longestConsecutive(root)
    print(res)
