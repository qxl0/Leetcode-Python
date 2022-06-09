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
    # nums = [1, 5, 10]
    # n = 20
    nums = [
        1,
        2,
        16,
        19,
        31,
        35,
        36,
        64,
        64,
        67,
        69,
        71,
        73,
        74,
        76,
        79,
        80,
        91,
        95,
        96,
        97,
    ]
    n = 8
    res = sol.minPatches(nums, n)
    print(res)
