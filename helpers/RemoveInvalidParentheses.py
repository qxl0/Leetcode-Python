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
    def removeInvalidParentheses(self, s: str) -> List[str]:
        count = 0
        remove = 0
        ret = []
        for ch in s:
            if ch == "(":
                count += 1
            elif ch == ")":
                count -= 1
            if count < 0:
                remove += 1
                count = 0
        remove += count
        maxLen = len(s) - remove

        def dfs(s, idx, curStr, cnt):
            if cnt < 0:
                return
            if len(curStr) > maxLen:
                return
            if idx == len(s):
                if count == 0 and len(curStr) == maxLen:
                    ret.append(curStr)
                return
            if s[idx] != "(" and s[idx] != ")":
                dfs(s, idx + 1, curStr + s[idx], cnt)
            else:
                if s[idx] == "(":
                    newCnt = cnt + 1
                else:
                    newCnt = cnt - 1
                dfs(s, idx + 1, curStr + s[idx], newCnt)
                if len(curStr) == 0 or s[idx] != curStr[-1]:
                    dfs(s, idx + 1, curStr, cnt)

        dfs(s, 0, "", 0)
        return ret


if __name__ == "__main__":
    sol = Solution()
    s = ")("
    res = sol.removeInvalidParentheses(s)
    print(res)
