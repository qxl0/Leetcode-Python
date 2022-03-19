from typing import List


class Solution:
    def productExceptSelf1(self, nums):
        left = [1] * len(nums)
        for i in range(1, len(nums)):
            left[i] = left[i - 1] * nums[i - 1]
        print(left)

        right = 1
        for i in range(len(nums) - 1, -1, -1):
            left[i] = left[i] * right
            right *= nums[i]
        print(left)

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        for i in range(1, len(nums)):
            res[i] = res[i - 1] * nums[i - 1]

        right = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= right
            right *= nums[i]

        return res


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3, 4, 5, 6]
    res = sol.productExceptSelf(nums)
    print(res)
