"""
759. Employee Free Time
Hard

2213. Longest Substring of One Repeating Character
Hard

109

68

Add to List

Share
You are given a 0-indexed string s. You are also given a 0-indexed string queryCharacters of length k and a 0-indexed array of integer indices queryIndices of length k, both of which are used to describe k queries.

The ith query updates the character in s at index queryIndices[i] to the character queryCharacters[i].

Return an array lengths of length k where lengths[i] is the length of the longest substring of s consisting of only one repeating character after the ith query is performed.
"""


from math import floor
from typing import List


class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end


class Solution:
    def longestRepeating(
        self, s: str, queryCharacters: str, queryIndices: List[int]
    ) -> List[int]:
        pass


if __name__ == "__main__":
    sol = Solution()
    s = ("babacc",)
    queryCharacters = "bcb"
    queryIndices = [1, 3, 3]
    res = sol.longestRepeating(s, queryCharacters, queryIndices)

    print(res)
