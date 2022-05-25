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
                tx, ty = points[j].x, points[j].y
                if tx == points[i].x and ty == points[i].y:
                    same += 1
                    continue
                if points[i].x == tx:
                    slope = "i"
                else:
                    slope = (points[i].y - ty) * 1.0 / (points[i].x - tx)
                if slope not in dic:
                    dic[slope] = 1
                dic[slope] += 1
            m = max(m, max(dic.values()) + same)
        return m


if __name__ == "__main__":
    sol = Solution()
    points = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]
    res = sol.maxPoints(points)
    print("Ans is: ", res)
