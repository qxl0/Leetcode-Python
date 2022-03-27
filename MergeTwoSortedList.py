"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""


import collections
import heapq
import random
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for singly-linked list.
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        i1, i2 = list1, list2
        list3 = i3 = ListNode(-1)
        while i1 and i2:
            val1, val2 = i1.val, i2.val
            if val1 < val2:
                i3.next = ListNode(val1)
                i3, i1 = i3.next, i1.next
            else:
                i3.next = ListNode(val2)
                i3, i2 = i3.next, i2.next
        while i1:
            i3.next = ListNode(i1.val)
            i3, i1 = i3.next, i1.next
        while i2:
            i3.next = ListNode(i2.val)
            i3, i2 = i3.next, i2.next
        return list3.next


if __name__ == "__main__":
    sol = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(4)
    list2 = ListNode(1)
    list2.next = ListNode(3)
    list2.next.next = ListNode(4)
    res = sol.mergeTwoLists(head, list2)
    print("result is: ", res)
