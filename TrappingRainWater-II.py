"""
407. Trapping Rain Water II
Hard

2702

61

Add to List

Share
Given an m x n integer matrix heightMap representing the height of each unit cell in a 2D elevation map, return the volume of water it can trap after raining.
"""

import collections
from math import floor
from typing import List


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    heightMap = [[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]]
    res = sol.trapRainWater(heightMap)
    print("Ans is: ", res)
