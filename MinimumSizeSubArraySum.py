from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        sum = 0
        ans = sys.maxsize
        for i in range(len(nums)):
            sum += nums[i]
            if sum >= target:
                ans = min(ans, i - left + 1)
                left += 1
                while left < len(nums) and sum - nums[left] >= target:
                    ans = min(ans, i - left + 1)
                    left += 1
        return ans


if __name__ == "__main__":
    s = Solution()
    # nums = [-2, 0, 1, 3]
    nums = [2, 3, 1, 2, 4, 3]
    target = 7
    res = s.minSubArrayLen(target, nums)
    print(res)
