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
        phoneMap = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz",
        }
        res = []
        if not digits:
            return res

        def helper(index, cur):
            if len(cur) == len(digits):
                res.append(cur)
                return
            str = phoneMap[int(digits[index])]
            for c in str:
                helper(index + 1, cur + c)

        helper(0, "")
        return res


if __name__ == "__main__":
    sol = Solution()
    digits = "238"
    res = sol.letterCombinations(digits)
    print(res)
