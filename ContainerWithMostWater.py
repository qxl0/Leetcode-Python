"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""


from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        pass


if __name__ == "__main__":
    s = Solution()
    heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    res = s.maxArea(heights)
    print(res)
