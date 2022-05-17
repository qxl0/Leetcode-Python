from typing import Optional
from helpers.TreeNode import TreeNode


class Solution:
    def treeToDoublyList(self, root: "Optional[TreeNode]") -> "Optional[TreeNode]":
        def helper(node):
            """
            left->node->right
            """
            nonlocal last, first
            if node:
                helper(node.left)
                if last:
                    last.right = node
                    node.left = last
                else:
                    first = node
                last = node
                helper(node.right)

        if not root:
            return None
        first, last = None, None
        helper(root)
        last.right = first
        first.left = last
        return first


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode.to_binary_tree([5, 3, 6, 2, 4, None, None, 1])
    res = sol.findLeaves(root)

    print(res)
