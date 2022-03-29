"""
103 · Linked List Cycle II
Algorithms
Hard
Accepted Rate
39%

DescriptionSolutionNotesDiscussLeaderboard
Description
Given a linked list, return the node where the cycle begins.

If there is no cycle, return null.


"""
from heapq import *
from lib2to3.pgen2.token import MINEQUAL
from typing import List, Optional


class ListNode:
    __eq__ = lambda self, other: self.val == other.val
    __lt__ = lambda self, other: self.val < other.val

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def detectCycle(self, head):
        pass


if __name__ == "__main__":
    s = Solution()
    head = ListNode(21)
    head.next = tail = ListNode(10)
    head.next.next = ListNode(4)
    head.next.next.next = ListNode(5)
    head.next.next.next.next = tail
    res = s.detectCycle(head)
    print(res)
