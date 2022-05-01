"""
1854. Maximum Population Year
Easy

552

80

Add to List

Share
You are given a 2D integer array logs where each logs[i] = [birthi, deathi] indicates the birth and death years of the ith person.

The population of some year x is the number of people alive during that year. The ith person is counted in year x's population if x is in the inclusive range [birthi, deathi - 1]. Note that the person is not counted in the year that they die.

Return the earliest year with the maximum population.
"""


from typing import List


class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    logs = [[1993, 1999], [2000, 2010]]
    res = sol.maximumPopulation(logs)

    print(res)
