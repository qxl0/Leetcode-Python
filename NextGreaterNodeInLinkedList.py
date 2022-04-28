"""
1019. Next Greater Node In Linked List
Medium

2120

96

Add to List

Share
You are given the head of a linked list with n nodes.

For each node in the list, find the value of the next greater node. That is, for each node, find the value of the first node that is next to it and has a strictly larger value than it.

Return an integer array answer where answer[i] is the value of the next greater node of the ith node (1-indexed). If the ith node does not have a next greater node, set answer[i] = 0.
"""


from math import floor
from typing import List, Optional
from helpers.LinkedList import LinkedList, ListNode


class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        pass


if __name__ == "__main__":
    sol = Solution()
    head = LinkedList.lst2link([2, 7, 4, 3, 5])
    res = sol.nextLargerNodes(head)
    print(res)
