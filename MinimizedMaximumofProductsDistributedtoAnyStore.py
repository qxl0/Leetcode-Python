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

from this import d
from typing import List, Optional


class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    n = 6
    quantities = [11, 6]
    res = sol.minimizedMaximum(n, quantities)
    print(res)
