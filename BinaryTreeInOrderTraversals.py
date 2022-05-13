# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional
from helpers.TreeNode import TreeNode


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res, stack = [], []
        cur = root
        while cur or stack:
            while cur:  # travel to each node's left child, till reach the left leaf
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()  # this node has no left child
            res.append(cur.val)  # so let's append the node value
            cur = cur.right
        return res


if __name__ == "__main__":
    sol = Solution()
    # s = [3, 9, 20, None, None, 15, 7]
    s = [1, None, 2, None, None, 3]
    root = TreeNode.to_binary_tree(s)
    res = sol.inorderTraversal(root)
    print("Ans is: ", res)
