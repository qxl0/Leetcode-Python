"""
84. Largest Rectangle in Histogram
Hard

9640

142

Add to List

Share
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.
"""


import enum
from typing import List, Optional
from helpers.LinkedList import Node


class Solution:
    def largestRectangleArea(self, height: List[int]) -> int:
        """
        Do not return anything, modify nums in-place instead.
        """
        height.append(0)
        stack = [-1]
        ans = 0
        for i in range(len(height)):
            while height[i] < height[stack[-1]]:
                h = height[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)
        height.pop()
        return ans


class Solution2:
    def largestRectangleArea(self, heights):
        maxArea = 0
        stack = []  # (start, height)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea


if __name__ == "__main__":
    sol = Solution2()
    heights = [2, 1, 5, 6, 2, 3]
    res = sol.largestRectangleArea(heights)
    print(res)
