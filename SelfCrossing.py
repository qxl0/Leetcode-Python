from typing import List

"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""


class Solution:
    def isSelfCrossing(self, distance: List[int]) -> bool:
        n = len(distance)
        x = distance
        for i, c in enumerate(3, n):
            if x[i] > x[i - 2] and x[i - 1] < x[i - 3]:
                return True
            if i >= 4:
                if x[i] + x[i - 4] > x[i - 2] and x[i - 1] == x[i - 3]:
                    return True
            if i >= 5:
                if (
                    x[i] >= x[i - 2] - x[i - 4]
                    and x[i - 1] >= x[i - 3] - x[i - 5]
                    and x[i - 2] > x[x - 4]
                    and x[i - 3] > x[i - 5]
                ):
                    return True
        return False


if __name__ == "__main__":
    s = Solution()
    x = [2, 1, 1, 2]
    res = s.isSelfCrossing(x)
    print(res)
