import heapq
from typing import List


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        q = []
        for i in range(len(primes)):
            heapq.heappush(q, (primes[i], primes[i], 0))

        nums = [0] * (n + 1)
        nums[0] = 1
        i = 1
        while i < n:
            num, p, idx = heapq.heappop(q)
            if num != nums[i - 1]:
                nums[i] = num
                i += 1
            heapq.heappush(q, (p * nums[idx + 1], p, idx + 1))
        print(nums)
        return nums[n - 1]


if __name__ == "__main__":
    sol = Solution()
    n = 12
    primes = [2, 7, 13, 19]
    res = sol.nthSuperUglyNumber(n, primes)
    print(res)
