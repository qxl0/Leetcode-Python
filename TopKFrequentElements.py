from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        pass


if __name__ == "__main__":
    s = Solution()
    # lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    nums = [1, 1, 1, 2, 2, 3]
    res = s.topKFrequent(nums)
    print(res)
