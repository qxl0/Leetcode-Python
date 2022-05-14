"""
1552. Magnetic Force Between Two Balls
Medium

1150

78

Add to List

Share
In the universe Earth C-137, Rick discovered a special form of magnetic force between two balls if they are put in his new invented basket. Rick has n empty baskets, the ith basket is at position[i], Morty has m balls and needs to distribute the balls into the baskets such that the minimum magnetic force between any two balls is maximum.

Rick stated that magnetic force between two different balls at positions x and y is |x - y|.

Given the integer array position and the integer m. Return the required force.
"""
from collections import defaultdict, deque
from typing import List, Optional

from helpers.TreeNode import TreeNode


class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        l, r = 1, position[-1] - position[0]

        def balls(f):
            # given force, count balls
            balls = 1
            prevpos = position[0]
            for i in range(1, len(position)):
                if position[i] - prevpos >= f:
                    prevpos = position[i]
                    balls += 1
            return balls

        while l + 1 < r:
            mid = l + (r - l) // 2  # force
            if balls(mid) >= m:
                l = mid
            else:
                r = mid
        return l


if __name__ == "__main__":
    sol = Solution()
    # position = [1, 2, 3, 4, 7]
    # m = 3
    # position = [5, 4, 3, 2, 1, 100000000]
    # m = 2
    position = [1, 2, 3, 4, 5, 100]
    m = 2
    res = sol.maxDistance(position, m)

    print(res)
