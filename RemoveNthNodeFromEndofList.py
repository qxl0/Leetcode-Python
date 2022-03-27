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

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
   


if __name__ == "__main__":
    s = Solution()
    head = [1,2,3,4,5]
    n = 2 
    res = s.removeNthFromEnd(head, n)
    print(res)
