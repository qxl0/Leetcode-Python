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
        ans = []

        def helper(node):
            if not node:
                return -1

            l = helper(node.left)
            r = helper(node.right)
            myheight = max(l, r) + 1
            if myheight >= len(ans):
                ans.append([])
            ans[myheight].append(node.val)
            return myheight

        helper(root)
        return ans


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode.to_binary_tree([5, 3, 6, 2, 4, None, None, 1])
    res = sol.findLeaves(root)

    print(res)
