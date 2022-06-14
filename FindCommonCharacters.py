from collections import Counter
from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = Counter(words[0])

        for word in words:
            res &= Counter(word)
        return list(res.elements())


if __name__ == "__main__":
    sol = Solution()
    words = ["bella", "label", "roller"]
    res = sol.commonChars(words)
    print(res)
