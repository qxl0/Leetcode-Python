"""
243. Shortest Word Distance
Easy

1002

85

Add to List

Share
Given an array of strings wordsDict and two different strings that already exist in the array word1 and word2, return the shortest distance between these two words in the list.
"""
from collections import defaultdict
import collections
from math import factorial
from operator import itemgetter
from typing import List


class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    wordsDict = ["practice", "makes", "perfect", "coding", "makes"]
    word1 = "coding"
    word2 = "practice"
    res = sol.shortestDistance(wordsDict, word1, word2)
    print(res)
