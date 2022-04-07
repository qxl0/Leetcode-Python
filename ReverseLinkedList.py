"""
Meeting Room 4
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] 
(si < ei) and the value of each meeting. You can only attend a meeting at the same time. Please calculate the most value you can get.
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


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        prev, curr = None, head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev


class Solution2:
    def reverseList(self, head):
        pre, curr = None, head
        while curr:
            # curr.next, curr, pre = pre, curr.next, curr
            pre, curr.next, curr = curr, pre, curr.next
        return pre


if __name__ == "__main__":
    sol = Solution2()
    head = ListNode(1)
    # head.next = ListNode(2)
    # head.next.next = ListNode(3)
    res = sol.reverseList(head)
    print("result is: ", res)
