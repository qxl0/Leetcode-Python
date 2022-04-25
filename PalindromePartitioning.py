from operator import truediv
from typing import List

"""
131. Palindrome Partitioning
Medium

6524

205

Add to List

Share
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.
"""


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def isPar(s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        def dfs(i, curr):
            if i >= len(s):
                res.append(curr)
                return
            for j in range(i, len(s)):
                if isPar(s, i, j):
                    dfs(j + 1, curr + [s[i : j + 1]])

        dfs(0, [])
        return res


if __name__ == "__main__":
    sol = Solution()
    s = "aab"
    res = sol.partition(s)
    print("Ans is:", res)
