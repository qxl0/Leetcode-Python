"""
116. Populating Next Right Pointers in Each Node
Medium

6258

229

Add to List

Share
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.
"""
from typing import Optional
from helpers.Node import Node


class Solution:
    max_path = float("-inf")

    def connect(self, root: "Optional[Node]") -> "Optional[Node]":
        pass


if __name__ == "__main__":
    sol = Solution()
    root = Node.to_binary_tree([-10, 9, 20, None, None, 15, 7])
    res = sol.maxPathSum(root)
    print("max Sum of the tree is", res)
