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
from helpers.LinkedList import ListNode


class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], l: int, r: int
    ) -> Optional[ListNode]:
        """
        Do not return anything, modify nums in-place instead.
        """
        dummy = ListNode(0)
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
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    res = sol.reverseBetween(head, 2, 4)
    print(res)
