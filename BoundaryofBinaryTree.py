"""
545. Boundary of Binary Tree
Medium

1067

1726

Add to List

Share
The boundary of a binary tree is the concatenation of the root, the left boundary, the leaves ordered from left-to-right, and the reverse order of the right boundary.

The left boundary is the set of nodes defined by the following:

The root node's left child is in the left boundary. If the root does not have a left child, then the left boundary is empty.
If a node in the left boundary and has a left child, then the left child is in the left boundary.
If a node is in the left boundary, has no left child, but has a right child, then the right child is in the left boundary.
The leftmost leaf is not in the left boundary.
The right boundary is similar to the left boundary, except it is the right side of the root's right subtree. Again, the leaf is not part of the right boundary, and the right boundary is empty if the root does not have a right child.

The leaves are nodes that do not have any children. For this problem, the root is not a leaf.

Given the root of a binary tree, return the values of its boundary.
"""


from typing import Optional
from helpers.TreeNode import TreeNode


class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        def getleafnodes(node):
            if not node:
                return
            if not node.left and not node.right:
                return [node.val]
            l = []
            if node.left:
                l = getleafnodes(node.left)
            r = []
            if node.right:
                r = getleafnodes(node.right)
            return l + r

        def getleft(node):
            if not node:
                return []
            ans = []
            if node.left:
                ans.append(node.val)
            if node.left:
                ans = ans + getleft(node.left)
            return ans

        def getright(node):
            if not node:
                return []
            ans = []
            if node.right:
                ans.append(node.val)
            if node.right:
                ans.extend(getright(node.right))
            return ans

        if not root:
            return []

        l = getleft(root)
        leaf = getleafnodes(root.left)
        r = getright(root.right)
        return [root.val] + l + leaf + r[::-1]


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
