"""
113. Path Sum II
Medium

4628

109

Add to List

Share
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.
"""


from typing import List, Optional
from helpers.TreeNode import TreeNode
from helpers.Node import Node


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        """
        Do not return anything, modify nums in-place instead.
        """
        ret = []

        def dfs(node, path, target):
            if not node:
                return
            if not node.left and not node.right and target == node.val:
                ret.append(path + [node.val])
                return

            dfs(node.left, path + [node.val], target - node.val)
            dfs(node.right, path + [node.val], target - node.val)

        dfs(root, [], targetSum)
        return ret


if __name__ == "__main__":
    sol = Solution()
    # root = TreeNode.to_binary_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])
    # targetSum = 22
    root = TreeNode.to_binary_tree([1, 2])
    targetSum = 1
    res = sol.pathSum(root, targetSum)
    print(res)
