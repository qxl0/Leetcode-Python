"""
897. Increasing Order Search Tree
Easy

3201

629

Add to List

Share
Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.
"""

import collections
from math import floor
from typing import List
from helpers.TreeNode import TreeNode


class Solution:
    def maxPoints(self, points):
        l = len(points)
        m = 0
        for i in range(l):
            dic = {"i": 1}
            same = 0
            for j in range(i + 1, l):
                tx, ty = points[j][0], points[j][1]
                if tx == points[i][0] and ty == points[i][1]:
                    same += 1
                    continue
                if points[i][0] == tx:
                    slope = "i"
                else:
                    slope = (points[i][1] - ty) * 1.0 / (points[i][0] - tx)
                if slope not in dic:
                    dic[slope] = 1
                dic[slope] += 1
            m = max(m, max(dic.values()) + same)
        return m


if __name__ == "__main__":
    sol = Solution()
    # points = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]
    points = [[1, 1], [2, 2], [2, 1], [3, 2]]
    res = sol.maxPoints(points)
    print("Ans is: ", res)
