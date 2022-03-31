import math
from typing import List

"""
784. Letter Case Permutation
Medium

3167

141

Add to List

Share
Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. Return the output in any order.
"""


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []

        def helper(s, i, curr, res):
            if len(curr) == len(s):
                res.append(curr)
                return
            if s[i].isdigit():
                helper(s, i + 1, curr + s[i], res)
                return
            helper(s, i + 1, curr + s[i].upper(), res)
            helper(s, i + 1, curr + s[i].lower(), res)

        helper(s, 0, "", res)
        return res


if __name__ == "__main__":
    s = Solution()
    str = "a1b2"
    res = s.letterCasePermutation(str)
    print(res)
