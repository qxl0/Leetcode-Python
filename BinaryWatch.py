"""
401. Binary Watch
Easy

935

1758

Add to List

Share
A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59). Each LED represents a zero or one, with the least significant bit on the right.

For example, the below binary watch reads "4:51".
"""
import collections
from typing import List, Optional
from helpers.TreeNode import TreeNode


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        res = []

        def bitcount(x):
            ret = 0
            while x:
                x = x & (x - 1)
                ret += 1
            return ret

        for hour in range(0, 12):
            for minute in range(0, 60):
                if bitcount(hour) + bitcount(minute) == turnedOn:
                    temp = str(hour) + ":"
                    if minute < 10:
                        temp += "0"
                    temp += str(minute)
                    res.append(temp)
        return res


if __name__ == "__main__":
    sol = Solution()
    turnedOn = 1
    res = sol.readBinaryWatch(turnedOn)
    print("Ans is ", res)
