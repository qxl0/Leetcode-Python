"""
703. Kth Largest Element in a Stream
Easy

2809

1668

Add to List

Share
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:

KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.
"""


import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.minq = nums
        heapq.heapify(self.minq)
        self.size = k
        while len(self.minq) > self.size:
            heapq.heappop(self.minq)

    def add(self, val: int) -> int:
        heapq.heappush(self.minq, val)
        while len(self.minq) > self.size:
            heapq.heappop(self.minq)
        print(f"Kth largest is: {self.minq[0]}")
        return self.minq[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# ["KthLargest", "add", "add", "add", "add", "add"]
# [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]

if __name__ == "__main__":
    k = 3
    nums = [4, 5, 8, 2]
    s = KthLargest(k, nums)
    s.add(3)
    s.add(5)
    s.add(10)
    s.add(9)
    s.add(4)
    print("Ans is: ", res)
