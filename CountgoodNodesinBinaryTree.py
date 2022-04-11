"""
1448. Count Good Nodes in Binary Tree
Medium

2232

74

Add to List

Share
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.
"""


from typing import List, Optional
from helpers.TreeNode import TreeNode


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    s = [3, 1, 4, 3, None, 1, 5]
    root = TreeNode.to_binary_tree(s)
    res = sol.goodNodes(root)
    print("Ans is: ", res)
