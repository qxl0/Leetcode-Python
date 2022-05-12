"""
863. All Nodes Distance K in Binary Tree
Medium

6180

127

Add to List

Share
Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.

You can return the answer in any order.

 
"""
import collections
import sys
from typing import List

from helpers.TreeNode import TreeNode


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        adj = collections.defaultdict(list)

        def toAdj(node, parent, adj):
            if not node:
                return
            if parent:
                adj[node].append(parent)
            if node.left:
                adj[node].append(node.left)
                toAdj(node.left, node, adj)
            if node.right:
                adj[node].append(node.right)
                toAdj(node.right, node, adj)

        def find(root, target):
            if not root:
                return None
            if root.val == target.val:
                return root
            left = find(root.left, target)
            if left:
                return left
            return find(root.right, target)

        toAdj(root, None, adj)

        # find target
        tnode = find(root, target)

        # get arry of the distance k node values
        ans = []
        level = 0
        vis = set()
        vis.add(tnode)
        q = [tnode]
        while q:
            qsize = len(q)
            for i in range(qsize):
                cur = q.pop(0)
                if level == k:
                    ans.append(cur.val)
                    continue
                vis.add(cur)
                # get ne
                for negi in adj[cur]:
                    if negi not in vis:
                        q.append(negi)
            level += 1
        return ans


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode.to_binary_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    target = TreeNode(5)
    K = 2
    res = sol.distanceK(root, target, K)
    print("Ans is : ", res)
