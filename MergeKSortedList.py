"""
23. Merge k Sorted Lists
Hard

11619

458

Add to List

Share
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.
Note: 

The problem while adding ListNode objects as tasks is that the Tuple comparison breaks for (priority, task) pairs if the priorities are equal and the tasks do not have a default comparison order. The solution is to store entries as 3-element list including the priority, an entry count, and the task.
The entry count serves as a tie-breaker so that two tasks with the same priority are returned in the order they were added.
And since no two entry counts are the same, the tuple comparison will never attempt to directly compare two tasks.


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
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minq = []
        for list in lists:
            for node in list:
                heappush(minq, (node.val, node))
        head = curr = ListNode(-1)
        while minq:
            node = heappop(minq)
            curr.next = ListNode(node.val)
            curr = curr.next
        return head.next


if __name__ == "__main__":
    s = Solution()
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    res = s.mergeKLists(lists)
    print(res)
