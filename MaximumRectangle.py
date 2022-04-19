"""
85. Maximal Rectangle
Hard

6481

106

Add to List

Share
Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.
"""


from typing import List, Optional
from helpers.LinkedList import Node


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not matrix or not matrix[0]:
            return 0
        n = len(matrix[0])
        height = [0] * (n + 1)
        ans = 0
        for row in matrix:
            for i in range(n):
                height[i] = height[i] + 1 if row[i] == "1" else 0
            stack = [-1]
            for i in range(n + 1):
                while height[i] < height[stack[-1]]:
                    h = height[stack.pop()]
                    w = i - 1 - stack[-1]
                    ans = max(ans, h * w)
                stack.append(i)
        return ans


class Solution2:
    def maximalRectangle(self, matrix):
        mxArea = 0
        m, n = len(matrix), len(matrix[0])
        heights = [0] * (n + 1)

        for row in matrix:
            for j in range(n):
                if row[j] == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0
            stack = []
            for i, h in enumerate(heights):
                while stack and heights[stack[-1]] > h:
                    H = heights[stack.pop()]
                    if stack:
                        w = i - stack[-1] - 1
                    else:
                        w = i
                    mxArea = max(mxArea, H * w)
                stack.append(i)
        return mxArea


if __name__ == "__main__":
    sol = Solution2()
    # matrix = [
    #     ["1", "0", "1", "0", "0"],
    #     ["1", "0", "1", "1", "1"],
    #     ["1", "1", "1", "1", "1"],
    #     ["1", "0", "0", "1", "0"],
    # ]
    matrix = [["1", "0"], ["1", "0"]]
    res = sol.maximalRectangle(matrix)
    print(res)
