"""
776. Split BST
Medium

894

90

Add to List

Share
Given the root of a binary search tree (BST) and an integer target, split the tree into two subtrees where one subtree has nodes that are all smaller or equal to the target value, while the other subtree has all nodes that are greater than the target value. It Is not necessarily the case that the tree contains a node with the value target.

Additionally, most of the structure of the original tree should remain. Formally, for any child c with parent p in the original tree, if they are both in the same subtree after the split, then node c should still have the parent p.

Return an array of the two roots of the two subtrees.
"""


from math import floor
from typing import List, Optional

from helpers.TreeNode import TreeNode


class Solution:
    def splitBST(
        self, root: Optional[TreeNode], target: int
    ) -> List[Optional[TreeNode]]:
        if not root:
            return [None, None]

        if root.val == target:
            right = root.right
            root.right = None
            return [root, right]

        elif root.val > target:
            A, B = self.splitBST(root.left, target)
            root.left = B  # this is the benefit of the recursion method, as the root if the parent of the subtree and is known
            return [A, root]
        else:
            A, B = self.splitBST(root.right, target)
            root.right = A
            return [root, B]


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode.to_binary_tree([4, 2, 6, 1, 3, 5, 7])
    target = 2
    res = sol.splitBST(root, target)
    print(res)
