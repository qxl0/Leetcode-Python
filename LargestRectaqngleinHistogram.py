"""
84. Largest Rectangle in Histogram
Hard

9640

142

Add to List

Share
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.
"""


from typing import List, Optional
from helpers.LinkedList import Node


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        Do not return anything, modify nums in-place instead.
        """


if __name__ == "__main__":
    sol = Solution()
    heights = [2, 1, 5, 6, 2, 3]
    res = sol.largestRectangleArea(heights)
    print(res)
