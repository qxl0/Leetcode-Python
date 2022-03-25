"""
892 · Alien Dictionary
Algorithms
Hard
Accepted Rate
28%

DescriptionSolutionNotesDiscussLeaderboard
Description
There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of 
non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.
You must write an algorithm that runs in O(n) time.
"""
import collections
from typing import List


class Solution:
    def alien_order(self, words: List[str]) -> str:
        # Write your code here
        pass


if __name__ == "__main__":
    sol = Solution()
    words = ["wrt", "wrf", "er", "ett", "rftt"]
    res = sol.alien_order(words)
    print("result is: ", res)
