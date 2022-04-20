"""
83. Remove Duplicates from Sorted List
Easy

4646

183

Add to List

Share
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
"""


from typing import List, Optional
from helpers.LinkedList import Node


class Solution:
    def deleteDuplicates(self, head: Optional[Node]) -> Optional[Node]:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not head:
            return None
        l, r = head, head.next
        while r:
            if r.value != l.value:
                l.next = r
                l = l.next
            r = r.next
        if l.next and l.value == l.next.value:
            l.next = None
        return head


if __name__ == "__main__":
    sol = Solution()
    head = Node(1)
    head.next = Node(1)
    head.next.next = Node(2)
    res = sol.deleteDuplicates(head)
    print(res)