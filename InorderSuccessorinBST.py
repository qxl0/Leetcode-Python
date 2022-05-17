from typing import Optional
from helpers.TreeNode import TreeNode


class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        prev = None
        successor = None
        found = False

        def inorder(node):
            nonlocal prev
            nonlocal successor
            nonlocal found
            if found:
                return
            if node.left:
                inorder(node.left)
            if prev == p:
                successor = node
                found = True
                return
            else:
                prev = node
            if node.right:
                inorder(node.right)

        if not root:
            return root
        inorder(root)
        return successor


class Solution2:
    def inorderSuccessor(self, root, p):
        succ = None
        while root:
            if root.val <= p.val:
                root = root.right
            else:
                succ = root
                root = root.left

        return succ


if __name__ == "__main__":
    sol = Solution2()
    root = TreeNode.to_binary_tree([5, 3, 6, 2, 4, None, None, 1])
    p = root.left.right
    res = sol.inorderSuccessor(root, p)

    print(res)
