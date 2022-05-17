"""
366. Find Leaves of Binary Tree
Medium

2422

43

Add to List

Share
Given the root of a binary tree, collect a tree's nodes as if you were doing this:

Collect all the leaf nodes.
Remove all the leaf nodes.
Repeat until the tree is empty.
"""
from typing import List, Optional
from helpers.TreeNode import TreeNode


class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        pass


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode.to_binary_tree([5, 3, 6, 2, 4, None, None, 1])
    res = sol.findLeaves(root)

    print(res)
