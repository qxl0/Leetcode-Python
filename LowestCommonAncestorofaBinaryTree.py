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
