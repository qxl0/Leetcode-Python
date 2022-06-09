from typing import List


class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patches, i = 0, 0

        miss = 1
        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                miss += miss
                patches += 1
        return patches


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 3]
    n = 6
    res = sol.minPatches(nums, n)
    print(res)
