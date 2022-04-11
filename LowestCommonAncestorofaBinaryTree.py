"""
236. Lowest Common Ancestor of a Binary Tree
Medium

9335

271

Add to List

Share
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor 
is defined between two nodes p and q as the lowest node in T that has both p and q as descendants 
(where we allow a node to be a descendant of itself).”
"""


# class TreeNode:
#     def __init__(self, val: int, left=None, right=None) -> None:
#         self.val = val
#         self.left = left
#         self.right = right

#     def __repr__(self) -> str:
#         return f"val: {self.val}, left: {self.left}, right: {self.right}"

#     def __str__(self) -> str:
#         return str(self.val)


# def to_binary_tree(items: list[int]) -> TreeNode:
#     """Create BT from list of values."""
#     n = len(items)
#     if n == 0:
#         return None

#     def inner(index: int = 0) -> TreeNode:
#         """Closure function using recursion bo build tree"""
#         if n <= index or items[index] is None:
#             return None

#         node = TreeNode(items[index])
#         node.left = inner(2 * index + 1)
#         node.right = inner(2 * index + 2)
#         return node

#     return inner()


from helpers.TreeNode import TreeNode


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        def dfs(curr):
            if not curr:
                return None
            if curr.val == p or curr.val == q:
                return curr
            left = dfs(curr.left)
            right = dfs(curr.right)

            if left and right:
                return curr

            return left if left else right

        return dfs(root)


if __name__ == "__main__":
    sol = Solution()
    # res = sol.lowestCommonAncestor(root, p, q)
    # s = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    # root = to_binary_tree(s)
    # p = 5
    # q = 1
    s = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    root = TreeNode.to_binary_tree(s)
    p = 5
    q = 4
    res = sol.lowestCommonAncestor(root, p, q)
    print("Ans is: ", res)
