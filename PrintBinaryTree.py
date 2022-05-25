# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional
from helpers.TreeNode import TreeNode


class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        if not root:
            return []

        def findHeight(node):
            return (
                0
                if not node
                else (1 + max(findHeight(node.left), findHeight(node.right)))
            )

        height = findHeight(root)
        width = 2**height - 1
        ans = [[""] * width for _ in range(height)]

        def output(node, row, left, right):
            if not node:
                return
            mid = (left + right) // 2
            ans[row][mid] = str(node.val)
            output(node.left, row + 1, left, mid - 1)
            output(node.right, row + 1, mid + 1, right)

        output(root, 0, 0, width - 1)
        return ans


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode.to_binary_tree([10, 5, 15, None, None, 6, 20])
    res = sol.printTree(root)
    print(res)
