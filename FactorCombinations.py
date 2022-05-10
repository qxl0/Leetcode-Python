"""
https://leetcode.com/problems/factor-combinations/#:~:text=254.%20Factor,n%20%2D%201%5D.
"""


import collections
import heapq
from math import sqrt
import random
from typing import List, Optional

from helpers.TreeNode import TreeNode


class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        if n == 1:
            return []
        ans = []

        def dfs(temp, product, index):
            if product == 1:
                ans.append(temp.copy())
                return
            for i in range(index, n // 2 + 1):
                if product % i == 0 and i != n:
                    temp.append(i)
                    dfs(temp, product // i, i)
                    temp.pop()

        dfs([], n, 2)
        return ans

    def getFactors2(self, n: int) -> List[List[int]]:
        if n == 1:
            return []
        ans = []

        def dfs(temp, product, index):
            if len(temp) > 0:
                temp.append(product)
                ans.append(temp.copy())
                temp.pop()
            for i in range(index, int(sqrt(product)) + 1):
                if product % i == 0 and i != n:
                    temp.append(i)
                    dfs(temp, product // i, i)
                    temp.pop()

        dfs([], n, 2)
        return ans


if __name__ == "__main__":
    sol = Solution()
    n = 12
    res = sol.getFactors2(n)
    print("result is: ", res)
