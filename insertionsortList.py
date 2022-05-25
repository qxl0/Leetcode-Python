"""
897. Increasing Order Search Tree
Easy

3201

629

Add to List

Share
Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.
"""

import collections
from math import floor
from typing import List, Optional
from helpers.TreeNode import TreeNode
from helpers.LinkedList import ListNode


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = head

        while cur:
            prev = dummy
            while prev.next and prev.next.val < cur.val:
                prev = prev.next

            nxt = cur.next

            cur.next = prev.next
            prev.next = cur

            cur.next = nxt

        return dummy.next


if __name__ == "__main__":
    sol = Solution()
    head = ListNode(4)
    head.next = ListNode(2)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(3)
    res = sol.insertionSortList(head)
    print("Ans is: ", res)
