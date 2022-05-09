"""
549. Binary Tree Longest Consecutive Sequence II
Medium

906

73

Add to List

Share
Given the root of a binary tree, return the length of the longest consecutive path in the tree.

A consecutive path is a path where the values of the consecutive nodes in the path differ by one. This path can be either increasing or decreasing.

For example, [1,2,3,4] and [4,3,2,1] are both considered valid, but the path [1,2,4,3] is not valid.
On the other hand, the path can be in the child-Parent-child order, where not necessarily be parent-child order.
"""

from math import inf
from this import d
from typing import List, Optional

from helpers.TreeNode import TreeNode


class Solution:
    def __init__(self):
        self.longest = 0

    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        longest = 1

        def helper(root):
            if not root:
                return (0, 0)
            dcr = inr = 1
            if root.left:
                left = helper(root.left)
                if root.left.val - 1 == root.val:
                    dcr = left[0] + 1
                elif root.left.val + 1 == root.val:
                    inr = left[1] + 1
            if root.right:
                right = helper(root.right)
                if root.right.val - 1 == root.val:
                    dcr = max(dcr, right[0] + 1)
                elif root.right.val + 1 == root.val:
                    inr = max(inr, right[1] + 1)
            longest = max(longest, inr + dcr - 1)
            return (dcr, inr)

        helper(root)
        return longest


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode.to_binary_tree([1, None, 3, 2, 4, None, None, None, 5])
    res = sol.longestConsecutive(root)
    print(res)
