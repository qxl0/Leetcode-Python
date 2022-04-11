"""
102. Binary Tree Level Order Traversal
Medium

7841

154

Add to List

Share
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
"""


from typing import List, Optional
from helpers.TreeNode import TreeNode


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ret = []
        if not root:
            return ret

        q = [root]
        while q:
            curr = []
            currq = []
            for i in q:
                curr.append(i.val)
                for kid in (i.left, i.right):
                    if kid:
                        currq.append(kid)
            ret.append(curr)
            q = currq
        return ret


class Solution_Recursive:
    def levelOrder(self, root):
        if not root:
            return []
        answer = []
        self.traverse(root, 1, answer)
        return answer

    def traverse(self, node, level, answer):
        if not node:
            return
        if level > len(answer):
            answer.append([node.val])
        else:
            answer[level - 1].extend([node.val])
        self.traverse(node.left, level + 1, answer)
        self.traverse(node.right, level + 1, answer)


if __name__ == "__main__":
    sol = Solution_Recursive()
    s = [3, 9, 20, None, None, 15, 7]
    root = TreeNode.to_binary_tree(s)
    res = sol.levelOrder(root)
    print("Ans is: ", res)
