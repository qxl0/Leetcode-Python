"""
199. Binary Tree Right Side View
Medium

6253

338

Add to List

Share
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
"""


from typing import List, Optional
from helpers.TreeNode import TreeNode


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ret = []
        if not root:
            return ret

        q = [root]
        while q:
            ret.append(q[-1].val)
            cur = []
            for n in q:
                for kid in (n.left, n.right):
                    if kid:
                        cur.append(kid)
            q = cur
        return ret

    def rightSideView2(self, root):
        if not root:
            return []

        right = self.rightSideView2(root.right)
        left = self.rightSideView2(root.left)
        return [root.val] + right + left[len(right) :]


if __name__ == "__main__":
    sol = Solution()
    s = [3, 9, 20, None, None, 15, 7]
    root = TreeNode.to_binary_tree(s)
    res = sol.rightSideView2(root)
    print("Ans is: ", res)
