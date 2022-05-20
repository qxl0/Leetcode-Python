from typing import Optional


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def inorderSuccessor(self, node: "Node") -> "Optional[Node]":
        def findRoot(node):
            if not node:
                return None
            while node.parent:
                node = node.parent
            return node

        target = node
        ans = None
        root = findRoot(node)
        prev = None

        def inorder(node):
            nonlocal ans, prev, target
            if not node:
                return
            if ans:
                return

            inorder(node.left)

            if prev == target:
                ans = node
                return
            else:
                prev = node

            inorder(node.right)

        inorder(root)
        return ans if ans else None


if __name__ == "__main__":
    sol = Solution()
    res = "11N2213314635736;57>6841988:<9;51<9;==<>:;"
    res2 = sol.deserialize(res)
    print(res2)
