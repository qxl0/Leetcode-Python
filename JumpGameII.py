"""
45. Jump Game II
Medium

7754

289

Add to List

Share
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.
"""
import sys
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n, start, end, step = len(nums), 0, 0, 0

        while end < n - 1:
            step += 1
            maxend = end + 1
            for i in range(start, end + 1):
                if i + nums[i] >= n - 1:
                    return step
                maxend = max(maxend, i + nums[i])
            start, end = end + 1, maxend
        return step


class Solution2:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return sys.maxsize
        if n == 1:
            return 0

        q = [0]
        visited = set()
        visited.add(0)
        level = 0

        while q:
            qsize = len(q)

            for i in range(qsize):
                currIdx = q.pop(0)
                j = min(n - 1, currIdx + nums[currIdx])
                while j > currIdx:
                    if j == n - 1:
                        return level + 1
                    if j not in visited:
                        visited.add(j)
                        q.append(j)
                    j -= 1
            level += 1
        return sys.maxsize


class Solution3:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return sys.maxsize
        if n == 1:
            return 0

        farest = 0
        step = 0
        curFarSofar = 0
        for i in range(n):
            farest = max(farest, i + nums[i])
            if i == curFarSofar:
                step += 1
                curFarSofar = max(curFarSofar, farest)
            if curFarSofar >= n - 1:
                return step
        return sys.maxsize


if __name__ == "__main__":
    s = Solution2()
    # nums = [3, 2, 1, 0, 4]
    # nums = [2, 3, 1, 1, 4]
    nums = [3, 4, 3, 2, 5, 4, 3]
    res = s.jump(nums)
    print("Ans is : ", res)
