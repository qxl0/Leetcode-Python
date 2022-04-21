"""
109. Convert Sorted List to Binary Search Tree
Medium

4494

113

Add to List

Share
Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
"""


from typing import List, Optional
from helpers.TreeNode import TreeNode
from helpers.Node import Node


class Solution:
    def sortedListToBST(self, head: Optional[Node]) -> Optional[TreeNode]:
        """
        Do not return anything, modify nums in-place instead.
        """


if __name__ == "__main__":
    sol = Solution()
    head = Node(-10)
    head.next = Node(-3)
    head.next.next = Node(0)
    head.next.next.next = Node(5)
    head.next.next.next.next = Node(9)
    res = sol.sortedListToBST(head)
    print(res)
