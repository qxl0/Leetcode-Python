from bisect import bisect_left
from collections import Counter
import heapq
from math import inf
from re import I
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Base case
        if len(arr) == k:
            return arr

        # Find the closest element and initialize two pointers
        left = bisect_left(arr, x) - 1
        right = left + 1

        # While the window size is less than k
        while right - left - 1 < k:
            # Be careful to not go out of bounds
            if left == -1:
                right += 1
                continue

            # Expand the window towards the side with the closer number
            # Be careful to not go out of bounds with the pointers
            if right == len(arr) or abs(arr[left] - x) <= abs(arr[right] - x):
                left -= 1
            else:
                right += 1

        # Return the window
        return arr[left + 1 : right]


if __name__ == "__main__":
    sol = Solution()
    arr = [1, 2, 3, 4, 5]
    k = 4
    res = sol.findClosestElements(arr, k)
    print(res)
