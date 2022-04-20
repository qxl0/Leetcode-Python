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
    def reverseBetween(
        self, head: Optional[Node], left: int, right: int
    ) -> Optional[Node]:
        """
        Do not return anything, modify nums in-place instead.
        """


if __name__ == "__main__":
    sol = Solution()
    head = Node(1)
    res = sol.reverseBetween(head)
    print(res)
