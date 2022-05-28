"""

"""

import collections
from math import floor
from typing import List, Optional
from helpers.TreeNode import TreeNode


class Solution:
    def computeArea(
        self,
        ax1: int,
        ay1: int,
        ax2: int,
        ay2: int,
        bx1: int,
        by1: int,
        bx2: int,
        by2: int,
    ) -> int:
        w = max(0, min(bx2, ax2) - max(bx1, ax1))
        h = max(0, min(by2, ay2) - max(by1, ay1))

        area1 = (ax2 - ax1) * (ay2 - ay1)
        area2 = (bx2 - bx1) * (by2 - by1)

        return area1 + area2 - w * h


if __name__ == "__main__":
    sol = Solution()
    ax1 = -3
    ay1 = 0
    ax2 = 3
    ay2 = 4
    bx1 = 0
    by1 = -1
    bx2 = 9
    by2 = 2
    res = sol.computeArea(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2)
    print("Ans is: ", res)
