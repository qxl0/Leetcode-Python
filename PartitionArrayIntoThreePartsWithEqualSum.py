from collections import Counter
from typing import List


class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:

        s = sum(arr)
        if s % 3 != 0:
            return False
        ans = 0
        cnt = 0
        for i in range(len(arr)):
            ans += arr[i]
            if ans == s // 3:
                cnt += 1
                ans = 0
        return ans == 0 and cnt >= 3


class Solution2:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        average, remainder, part, cnt = sum(A) // 3, sum(A) % 3, 0, 0
        for a in A:
            part += a
            if part == average:
                cnt += 1
                part = 0
        return not remainder and cnt >= 3


if __name__ == "__main__":
    sol = Solution()
    # arr = [3, 3, 6, 5, -2, 2, 5, 1, -9, 4]
    arr = [1, -1, 1, -1]
    res = sol.canThreePartsEqualSum(arr)
    print(res)
