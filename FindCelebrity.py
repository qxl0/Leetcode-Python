from collections import Counter
from typing import List


class Solution:
    def findCelebrity(self, n: int) -> int:
        degree = [0] * n
        for i in range(n):
            for j in range(i + 1, n):
                if knows(i, j):
                    degree[j] += 1
        print(degree)
        res = [i for i in degree if degree[i] == n]
        if len(res) == 1:
            return res[0]
        else:
            return -1


if __name__ == "__main__":
    sol = Solution()
    n = 3
    res = sol.findCelebrity(n)
    print(res)
