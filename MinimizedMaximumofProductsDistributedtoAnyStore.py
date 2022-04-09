"""
2064. Minimized Maximum of Products Distributed to Any Store
Medium

392

16

Add to List

Share
You are given an integer n indicating there are n specialty retail stores. There are m product types of varying amounts, which are given as a 0-indexed integer array quantities, where quantities[i] represents the number of products of the ith product type.

You need to distribute all products to the retail stores following these rules:

A store can only be given at most one product type but can be given any amount of it.
After distribution, each store will have been given some number of products (possibly 0). Let x represent the maximum number of products given to any store. You want x to be as small as possible, i.e., you want to minimize the maximum number of products that are given to any store.
Return the minimum possible x.
"""

from statistics import quantiles
from this import d
from typing import List, Optional


class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        l, r = 1, max(quantities)
        while l < r:
            mid = l + (r - l) // 2
            if self.checkOK(n, quantities, mid):
                r = mid
            else:
                l = mid + 1
        return l

    def checkOK(self, n, quantities, mid):
        total = 0
        for q in quantities:
            if q % mid == 0:
                total += q // mid
            else:
                total += q // mid + 1
        return total <= n


class Solution2:
    def minimizedMaximum(self, n, A):
        left, right = 1, max(A)
        while left < right:
            x = (left + right) // 2
            if sum((a + x - 1) // x for a in A) > n:
                left = x + 1
            else:
                right = x
        return left


if __name__ == "__main__":
    sol = Solution()
    # n = 6
    # quantities = [11, 6]
    # n = 7
    # quantities = [15, 10, 10]
    n = 1
    quantities = [1]
    res = sol.minimizedMaximum(n, quantities)
    print(res)
