"""
148. Sort List
Medium

7016

230

Add to List

Share
Given the head of a linked list, return the list after sorting it in ascending order.
"""


from typing import List, Optional
from helpers.LinkedList import LinkedList
from helpers.TreeNode import TreeNode


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Do not return anything, modify nums in-place instead.
        """


if __name__ == "__main__":
    sol = Solution()
    head = LinkedList.lst2link([4, 2, 3, 1])
    res = sol.sortList(head)
    print(res)
