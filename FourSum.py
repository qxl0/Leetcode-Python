from collections import defaultdict, deque
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)

        def Ksum(nums, target, k):
            res = []
            if not nums:
                return res
            avg_val = target // k
            if avg_val < nums[0] or nums[-1] < avg_val:
                return res
            if k == 2:
                return Twosum(nums, target)

            for i in range(len(nums)):
                if i == 0 or nums[i - 1] != nums[i]:
                    for subset in Ksum(nums[i + 1 :], target - nums[i], k - 1):
                        res.append([nums[i]] + subset)
            return res

        def Twosum(nums, target):
            res = []
            l, h = 0, len(nums) - 1
            while l < h:
                cur = nums[l] + nums[h]
                if cur < target or (l > 0 and nums[l] == nums[l - 1]):
                    l += 1
                elif cur > target or (h < len(nums) - 1 and nums[h] == nums[h + 1]):
                    h -= 1
                else:
                    res.append([nums[l], nums[h]])
                    l += 1
                    h -= 1
            return res

        nums.sort()
        return Ksum(nums, target, 4)


if __name__ == "__main__":
    sol = Solution()
    nums = [2, 2, 2, 2]
    target = 8
    res = sol.fourSum(nums, target)
    print(res)
