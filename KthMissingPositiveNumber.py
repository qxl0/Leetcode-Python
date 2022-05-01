"""
1539. Kth Missing Positive Number
Easy

2439

177

Add to List

Share
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Find the kth positive integer that is missing from this array.
"""


from math import floor
from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        count = 0
        for i, n in enumerate(arr):
            if i == 0:
                if n > k:
                    return k
                count += n - 1
            else:
                count += n - arr[i - 1] - 1
            if count >= k:
                # between arr[i-1], n
                return arr[i] - (count - k) - 1
        return arr[-1] + k - count


if __name__ == "__main__":
    sol = Solution()
    # arr = [2, 3, 4, 7, 11]
    # k = 5
    # arr = [1, 3]
    # k = 1
    arr = [1, 10, 21, 22, 25]
    k = 12
    res = sol.findKthPositive(arr, k)

    print(res)
