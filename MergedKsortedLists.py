from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pass


if __name__ == "__main__":
    s = Solution()
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    res = s.mergeKLists(lists)
    print(res)
