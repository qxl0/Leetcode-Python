from collections import Counter
import heapq
from typing import List


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        c = Counter(s)
        pos = 0
        for i in range(len(s)):
            if s[i] < s[pos]:
                pos = i
            c[s[i]] -= 1
            if c[s[i]] == 0:
                break
        return (
            s[pos] + self.removeDuplicateLetters(s[pos:].replace(s[pos], ""))
            if s
            else ""
        )


if __name__ == "__main__":
    sol = Solution()
    s = "cbacdcbca"
    res = sol.removeDuplicateLetters(s)
    print(res)
