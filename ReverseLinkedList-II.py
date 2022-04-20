"""
92. Reverse Linked List II
Medium

5961

279

Add to List

Share
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.
"""


from typing import List, Optional
from helpers.LinkedList import Node


class Solution:
    def reverseBetween(self, head: Optional[Node], l: int, r: int) -> Optional[Node]:
        """
        Do not return anything, modify nums in-place instead.
        """
        dummy = Node(0)
        dummy.next = head

        leftPrev, left = dummy, head
        for _ in range(l - 1):
            leftPrev, left = left, left.next

        #
        prev, curr = None, left
        for i in range(r - l + 1):
            tmpNext = curr.next
            curr.next = prev
            prev = curr
            curr = tmpNext

        # Hook up leftPrev = 1, prev = 4, curr = 5
        leftPrev.next.next = curr
        leftPrev.next = prev

        return dummy.next


if __name__ == "__main__":
    sol = Solution()
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    res = sol.reverseBetween(head, 2, 4)
    print(res)
