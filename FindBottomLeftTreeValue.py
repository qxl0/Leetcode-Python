from typing import Optional
from helpers.TreeNode import TreeNode


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        maxH = float("-inf")
        leftmost = 0

        def helper(node, height):
            nonlocal leftmost, maxH
            if not node:
                return
            helper(node.left, height + 1)
            helper(node.right, height + 1)

            if height > maxH:
                leftmost = node.val
                maxH = height

        helper(root, 0)
        return leftmost


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode.to_binary_tree([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1])
    res = sol.findBottomLeftValue(root)

    print(res)
