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


class Solution2:
    def treeToDoublyList(self, root: "Optional[Node]") -> "Optional[Node]":
        def helper(node):
            if not node:
                return (None, None)
            curfirst = node
            if node.left:
                lfirst, llast = helper(node.left)
                node.left = llast
                llast.right = node
                curfirst = lfirst
            curlast = node
            if node.right:
                rfirst, rlast = helper(node.right)
                node.right = rfirst
                rfirst.left = node
                curlast = rlast
            # print(node.val,":  ",curfirst.val,curlast.val)
            return (curfirst, curlast)

        if not root:
            return None
        first, last = helper(root)
        if first:
            first.left = last
        if last:
            last.right = first
        return first


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode.to_binary_tree([5, 3, 6, 2, 4, None, None, 1])
    res = sol.treeToDoublyList(root)

    print(res)
