"""
450. Delete Node in a BST
Medium

5307

157

Add to List

Share
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node
"""


from math import floor
from typing import List, Optional

from helpers.TreeNode import TreeNode


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # find the node
            if not (root.left or root.right):
                root = None
                return root
            elif not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                temp = root.right
                mini = temp.val
                while temp.left:
                    temp = temp.left
                    mini = temp.val
                root.val = mini
                root.right = self.deleteNode(root.right, mini)
        return root


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode.to_binary_tree([5, 3, 6, 2, 4, None, 7])
    key = 3
    res = sol.deleteNode(root, key)
    print(res)
