"""
1553. Minimum Number of Days to Eat N Oranges
Hard

647

41

Add to List

Share
There are n oranges in the kitchen and you decided to eat some of these oranges every day as follows:

Eat one orange.
If the number of remaining oranges n is divisible by 2 then you can eat n / 2 oranges.
If the number of remaining oranges n is divisible by 3 then you can eat 2 * (n / 3) oranges.
You can only choose one of the actions per day.

Given the integer n, return the minimum number of days to eat n oranges.
"""


import sys
from typing import List, Optional
from helpers.LinkedList import LinkedList
from helpers.LinkedList import ListNode
from helpers.TreeNode import TreeNode


class Solution:
    def minDays(self, n: int) -> int:
        dp = {0: 1, 1: 1}

        def dfs(n):
            if n in dp:
                return dp[n]
            way1 = 1 + (n % 2) + dfs(n // 2)
            way2 = 1 + (n % 3) + dfs(n // 3)

            dp[n] = min(way1, way2)
            return dp[n]

        return dfs(n)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

if __name__ == "__main__":
    sol = Solution()
    res = sol.minDays(10)
    print(res)
