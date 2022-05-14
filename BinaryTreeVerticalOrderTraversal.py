"""
314. Binary Tree Vertical Order Traversal
Medium

2421

264

Add to List

Share
Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.
"""
from collections import defaultdict, deque
from typing import List, Optional

from helpers.TreeNode import TreeNode


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = defaultdict(list)
        queue = deque([(root, 0)])
        while queue:
            node, col = queue.popleft()
            if node:
                ans[col].append(node.val)
                queue.append((root.left, col - 1))
                queue.append((root.right, col + 1))
        return [ans[x] for x in sorted(ans.keys())]


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode.to_binary_tree([3, 9, 20, None, None, 15, 7])
    res = sol.verticalOrder(root)

    print(res)
