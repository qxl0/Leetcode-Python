from collections import Counter, deque
from heapq import heapify, heappush, heappop


from bisect import bisect, bisect_left
from itertools import zip_longest
from typing import List


class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        nums = [int(w) for w in s.split() if w.isdigit()]
        return all(nums[i - 1] < nums[i] for i in range(1, len(nums)))


if __name__ == "__main__":
    sol = Solution()
    s = "3 leetcode questions got 1000 scores"
    res = sol.areNumbersAscending(s)
    print("result is: ", res)
