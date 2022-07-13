from collections import defaultdict, deque
from typing import List


class Solution:
    def fourSumCount(
        self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]
    ) -> int:
        m = defaultdict(list)
        lsts = [nums1, nums2, nums3, nums4]

        def nSumCount():
            add2map(0, 0)
            return countComplement(len(lsts) // 2, 0)

        def add2map(i, total):
            if i == len(lsts) // 2:
                m[total] += 1
            else:
                for a in lsts[i]:
                    add2map(i + 1, total + a)

        def countComplement(i, complement):
            if i == len(lsts):
                return m[complement]
            cnt = 0
            for a in lsts[i]:
                cnt += countComplement(i + 1, complement - a)
            return cnt

        return nSumCount()


if __name__ == "__main__":
    sol = Solution()
    A = [1, 2]
    B = [-2, -1]
    C = [-1, 2]
    D = [0, 2]
    res = sol.fourSumCount(A, B, C, D)
    print(res)
