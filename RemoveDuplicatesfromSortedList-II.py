"""
82. Remove Duplicates from Sorted List II
Medium

5615

164

Add to List

Share
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.
"""


from typing import List, Optional
from helpers.LinkedList import Node


class Solution:
    def deleteDuplicates(self, head: Optional[Node]) -> Optional[Node]:
        """
        Do not return anything, modify nums in-place instead.
        """
        dummy = Node(0)
        dummy.next = head
        pre, cur = dummy, head
        while cur and cur.next:
            if cur.value == cur.next.value:
                while cur and cur.next and cur.value == cur.next.value:
                    cur = cur.next
                pre.next = cur.next
            else:
                pre = pre.next

            cur = cur.next
        return dummy.next


if __name__ == "__main__":
    sol = Solution()
    head = Node(1)
    head.next = Node(1)
    head.next.next = Node(2)

    res = sol.deleteDuplicates(head)
    print(res)