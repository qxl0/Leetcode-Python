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

from this import d
from typing import List, Optional


class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        map1, map2 = {}, {}

        def dfs(x, y, p, s):
            # x --> index in p
            # y --> index in s
            if x == len(p) and y == len(s):
                return True
            ch = p[x]
            if ch in map1:
                t = map1[ch]
                if y + len(t) > len(s):
                    return False
                if s[y : y + len(t)] != t:
                    return False
                return dfs(x + 1, y + len(t), p, s)
            else:
                for i in range(y, len(s)):
                    t = s[y : i + 1]
                    if t in map2:
                        continue
                    map1[ch] = t
                    map2[t] = ch
                    if dfs(x + 1, y + len(t), p, s):
                        return True
                    del map1[ch]
                    del map2[t]
            return False

        return dfs(0, 0, pattern, s)


if __name__ == "__main__":
    sol = Solution()
    # p = "abab"
    # s = "asdasdasdasd"
    p = "ab"
    s = "cd"
    res = sol.wordPatternMatch(p, s)
    print(res)
