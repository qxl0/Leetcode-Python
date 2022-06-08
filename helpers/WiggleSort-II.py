from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0] * 5001

        for n in nums:
            count[n] += 1

        odd, even = 1, 0
        for n in range(5000, -1, -1):
            if odd >= len(nums) and even >= len(nums):
                break

            if count[n] == 0:
                continue

            while count[n] and (odd < len(nums) or even < len(nums)):
                count[n] -= 1
                if odd < len(nums):
                    nums[odd] = n
                    odd += 2
                else:
                    nums[even] = n
                    even += 2


if __name__ == "__main__":
    sol = Solution()
    # nums = [2, 2, 2, 2, 4, 4, 4]
    nums = [1, 5, 1, 1, 6, 4]
    res = sol.wiggleSort(nums)
    print(res)
