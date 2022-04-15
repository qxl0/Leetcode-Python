"""
1899. Merge Triplets to Form Target Triplet
Medium

291

23

Add to List

Share
A triplet is an array of three integers. You are given a 2D integer array triplets, where triplets[i] = [ai, bi, ci] describes the ith triplet. You are also given an integer array target = [x, y, z] that describes the triplet you want to obtain.

To obtain target, you may apply the following operation on triplets any number of times (possibly zero):

Choose two indices (0-indexed) i and j (i != j) and update triplets[j] to become [max(ai, aj), max(bi, bj), max(ci, cj)].
For example, if triplets[i] = [2, 5, 3] and triplets[j] = [1, 7, 5], triplets[j] will be updated to [max(2, 1), max(5, 7), max(3, 5)] = [2, 7, 5].
Return true if it is possible to obtain the target triplet [x, y, z] as an element of triplets, or false otherwise.
"""
import collections
import heapq
import sys
from typing import List


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        w = [0, 0, 0]
        t1, t2, t3 = target
        for a, b, c in triplets:
            if a <= t1 and b <= t2 and c <= t3:
                w[0] = max(w[0], a)
                w[1] = max(w[1], b)
                w[2] = max(w[2], c)
        return w[0] == t1 and w[1] == t2 and w[2] == t3


if __name__ == "__main__":
    s = Solution()
    triplets = [[2, 5, 3], [1, 8, 4], [1, 7, 5]]
    target = [2, 7, 5]
    res = s.mergeTriplets(triplets, target)
    print("Ans is : ", res)
