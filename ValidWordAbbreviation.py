"""

"""


from math import floor
from typing import List


class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = j = 0
        while i < len(word) and j < len(abbr):
            if abbr[j].isalpha() and abbr[j] == word[i]:
                j += 1
                i += 1
            elif abbr[j].isdigit():
                num = int(abbr[j])
                while j + 1 < len(abbr) and abbr[j + 1].isdigit():
                    num = num * 10 + int(abbr[j + 1])
                    j += 1
                i += num
                j += 1
            else:
                return False
        return True


if __name__ == "__main__":
    sol = Solution()
    word = "apple"
    abbr = "a2e"
    res = sol.validWordAbbreviation(word, abbr)
    print(res)
