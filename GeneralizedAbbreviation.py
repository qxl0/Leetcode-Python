from collections import Counter, deque
import heapq
from typing import List


class Solution:
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """

        def helper(word, pos, cur, count, result):
            if len(word) == pos:
                # Once we reach the end, append current to the result
                result.append(cur + str(count) if count > 0 else cur)
            else:
                # Skip current position, and increment count
                helper(word, pos + 1, cur, count + 1, result)
                # Include current position, and zero-out count
                helper(
                    word,
                    pos + 1,
                    cur + (str(count) if count > 0 else "") + word[pos],
                    0,
                    result,
                )

        result = []
        helper(word, 0, "", 0, result)
        return result


if __name__ == "__main__":
    sol = Solution()
    word = "word"
    res = sol.generateAbbreviations(word)
    print(res)
