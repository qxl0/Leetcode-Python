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
    def connect_bfs(self, root: "Optional[Node]") -> "Optional[Node]":
        if not root:
            return root
        q = [root]
        while q:
            cur = []
            for i in range(1, len(q)):
                q[i - 1].next = q[i]
                print(f"{q[i-1]}->{q[i]}")
                if q[i - 1].left:
                    cur.append(q[i - 1].left)
                    cur.append(q[i - 1].right)
            if q[len(q) - 1].left:
                cur.append(q[len(q) - 1].left)
                cur.append(q[len(q) - 1].right)
            q = cur
        return root

    def connect_recursive(self, root):
        if not root or not root.left:
            return root
        print(f"{root.left}->{root.right}")
        root.left.next = root.right
        if root.next:
            root.right.next = root.next.left
            print(f"{root.right}->{root.next.left}")
        self.connect_recursive(root.left)
        self.connect_recursive(root.right)
        return root

    def connect_iterative(self, root: "Optional[Node]") -> "Optional[Node]":
        head = root
        while root:
            cur, root = root, root.left
            while cur:
                if cur.left:
                    print(f"{cur.left}->{cur.right}")
                    cur.left.next = cur.right
                    if cur.next:
                        print(f"{cur.right}->{cur.next.left}")
                        cur.right.next = cur.next.left
                else:
                    break
                cur = cur.next
        return head

    def connect_bfs_interative(self, root: "Node") -> "Node":

        if not root:
            return None

        nodes_at_each_level = []
        level = [root]

        while level:
            nodes_at_each_level.append([node for node in level])
            level = [
                child for node in level for child in (node.left, node.right) if child
            ]

        # return root

        for level_nodes in nodes_at_each_level:
            for idx in range(len(level_nodes) - 1):
                level_nodes[idx].next = level_nodes[idx + 1]

        return root


if __name__ == "__main__":
    sol = Solution()
    root = Node.to_binary_tree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
    res = sol.connect_bfs_interative(root)
    print("Ans is ", res)
