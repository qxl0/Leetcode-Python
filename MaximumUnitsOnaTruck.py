"""
1710. Maximum Units on a Truck
Easy

1532

104

Add to List

Share
You are assigned to put some amount of boxes onto one truck. You are given a 2D array boxTypes, where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:

numberOfBoxesi is the number of boxes of type i.
numberOfUnitsPerBoxi is the number of units in each box of the type i.
You are also given an integer truckSize, which is the maximum number of boxes that can be put on the truck. You can choose any boxes to put on the truck as long as the number of boxes does not exceed truckSize.

Return the maximum total number of units that can be put on the truck.
"""


from math import floor
from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    boxTypes = [[1, 3], [2, 2], [3, 1]]
    truckSize = 4
    res = sol.maximumUnits(boxTypes, truckSize)

    print(res)
