from collections import defaultdict, deque
import functools
from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        vis = [0] * len(nums)  # len(nums) <=16

        @functools.lru_cache
        def dfs(cur, subs, sum):
            if subs == k:
                return True
            if sum > total // k:
                return False
            if sum == total // k:
                return dfs(0, subs + 1, 0)

            for i in range(cur, len(nums)):
                if vis[i] == 1:
                    continue
                vis[i] = 1
                if dfs(i + 1, subs, sum + nums[i]):
                    return True
                vis[i] = 0
            return False

        return dfs(0, 0, 0)


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 1, 1, 2, 2, 2]
    k = 3
    res = sol.canPartitionKSubsets(nums, k)
    print(res)
