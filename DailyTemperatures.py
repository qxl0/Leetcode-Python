"""
739. Daily Temperatures
Medium

6833

158

Add to List

Share
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.
"""


from math import floor
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                idx, v = stack.pop()
                ans[idx] = i - idx
            stack.append([i, t])
        return ans


if __name__ == "__main__":
    sol = Solution()
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    res = sol.dailyTemperatures(temperatures)
    print(res)
