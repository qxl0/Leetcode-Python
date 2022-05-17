from collections import defaultdict
from typing import Optional

from helpers.TreeNode import TreeNode


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        h = defaultdict(int)
        count = 0
        k = targetSum

        def helper(node, curr):
            nonlocal count
            if not node:
                return

            curr += node.val

            if curr == k:
                count += 1

            count += h[curr - k]

            h[curr] += 1

            helper(node.left, curr)
            helper(node.right, curr)

            h[curr] -= 1

        helper(root, 0)
        return count


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode.to_binary_tree([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1])
    targetSum = 8
    res = sol.pathSum(root, targetSum)

    print(res)
