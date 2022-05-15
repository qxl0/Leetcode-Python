# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
from helpers.TreeNode import TreeNode


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def depth(node):
            d = 0
            while node.left:
                node = node.left
                d += 1
            return d

        def exists(idx, d, node):
            left, right = 0, 2**d - 1
            for _ in range(d):
                mid = left + (right - left) // 2
                if idx <= mid:
                    node = node.left
                    right = mid
                else:
                    node = node.right
                    left = mid + 1
            return node is not None

        if not root:
            return 0
        d = depth(root)
        if d == 0:
            return 1
        left, right = 1, 2**d - 1
        while left <= right:
            mid = left + (right - left) // 2
            if exists(mid, d, root):
                left = mid + 1
            else:
                right = mid - 1
        return (2**d - 1) + left


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode.to_binary_tree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
    res = sol.countNodes(root)

    print(res)
