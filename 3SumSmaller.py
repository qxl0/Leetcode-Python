from typing import List


class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        if len(nums) < 3:
            return 0
        ans = 0
        nums.sort()
        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            while j < k:
                sum3 = nums[i] + nums[j] + nums[k]
                if sum3 < target:
                    ans += k - j
                if sum3 >= target:
                    k -= 1
                else:
                    j += 1
        return ans


class Solution2:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i >= 1 and nums[i] == nums[i - 1]:
                continue
            val = 0 - nums[i]
            # find j,k s.t. nums[j]+nums[k] = val
            j, k = i + 1, len(nums) - 1
            while j < k:
                if nums[j] + nums[k] > val:
                    k -= 1
                elif nums[j] + nums[k] < val:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
        return res


if __name__ == "__main__":
    # s = Solution()
    # nums = [-2, 0, 1, 3]
    # nums = [-1, 1, -1, -1]
    # target = -1
    # res = s.threeSumSmaller(nums, target)
    sol = Solution2()
    # nums = [0, 0, 0, 0]
    # nums = [-1, 0, 1, 2, -1, -4]
    nums = [-2, 0, 1, 1, 2]
    res = sol.threeSum(nums)
    print(res)
