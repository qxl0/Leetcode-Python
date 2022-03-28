"""
19. Remove Nth Node From End of List
Medium

9340

441

Add to List

Share
Given the head of a linked list, remove the nth node from the end of the list and return its head.
"""
from heapq import *
from lib2to3.pgen2.token import MINEQUAL
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        res = ListNode(0)
        res.next = head
        tmp = res

        for i in range(n):
            head = head.next

        while head != None:
            head = head.next
            tmp = tmp.next

        tmp.next = tmp.next.next
        return res.next


if __name__ == "__main__":
    s = Solution()
    # head = ListNode(0)
    # head.next = ListNode(1)
    # head.next.next = ListNode(2)
    # head.next.next.next = ListNode(3)
    # head.next.next.next.next = ListNode(4)
    # head.next.next.next.next.next = ListNode(5)
    # res = s.removeNthFromEnd(head.next, n)
    n = 2
    head = ListNode(1)
    n = 1
    res = s.removeNthFromEnd(head, n)
    # Output: [1,2,3,5]
    print(res)
