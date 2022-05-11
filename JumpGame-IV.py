"""
1345. Jump Game IV
Hard

1801

72

Add to List

Share
Given an array of integers arr, you are initially positioned at the first index of the array.

In one step you can jump from index i to index:

i + 1 where: i + 1 < arr.length.
i - 1 where: i - 1 >= 0.
j where: arr[i] == arr[j] and i != j.
Return the minimum number of steps to reach the last index of the array.

Notice that you can not jump outside of the array at any time.
"""
import sys
from typing import List


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        pass


if __name__ == "__main__":
    s = Solution()
    arr = [100, -23, -23, 404, 100, 23, 23, 23, 3, 404]
    res = s.minJumps(arr)
    print("Ans is : ", res)
