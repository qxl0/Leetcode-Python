"""
86. Partition List
Medium

3383

475

Add to List

Share
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.
"""


from typing import List, Optional
from helpers.LinkedList import Node


class Solution:
    def partition(self, head: Optional[Node], x: int) -> Optional[Node]:
        """
        Do not return anything, modify nums in-place instead.
        """


if __name__ == "__main__":
    sol = Solution()
    head = Node(1)
    head.next = Node(4)
    head.next.next = Node(3)
    head.next.next.next = Node(2)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(2)
    res = sol.partition(head)
    print(res)
