from operator import truediv

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
        pass


if __name__ == "__main__":
    s = Solution()
    s = "aab"
    res = s.partition(s)
    print("Word exists: ", res)
