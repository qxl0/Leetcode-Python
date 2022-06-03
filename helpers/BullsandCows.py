"""
36. Valid Sudoku
Medium

4793

692

Add to List

Share
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
"""

from collections import defaultdict
from this import d
from typing import List, Optional


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        h = defaultdict(int)
        x = y = 0

        for i, s in enumerate(secret):
            g = guess[i]

            if s == g:
                x += 1
            else:
                y += int(h[s] < 0) + int(h[g] > 0)
                h[s] += 1
                h[g] -= 1
        return "{}A{}B".format(x, y)


if __name__ == "__main__":
    sol = Solution()
    s = "1807"
    g = "7810"
    sol.getHint(s, g)
    res = sol.wordPatternMatch(p, s)
    print(res)
