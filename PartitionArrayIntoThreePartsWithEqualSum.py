from collections import Counter
from typing import List


class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:

        s = sum(arr)
        if s % 3 != 0:
            return False
        ans = 0
        for i in range(len(arr)):
            if ans > s // 3:
                return False
            elif ans == s // 3:
                ans = 0
            ans += arr[i]
        return True


if __name__ == "__main__":
    sol = Solution()
    arr = [3, 3, 6, 5, -2, 2, 5, 1, -9, 4]
    res = sol.canThreePartsEqualSum(arr)
    print(res)
