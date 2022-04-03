"""
17. Letter Combinations of a Phone Number
Medium

9474

659

Add to List

Share
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
"""


from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        pass


if __name__ == "__main__":
    sol = Solution()
    digits = "23"
    res = sol.letterCombinations(digits)
    print(res)
