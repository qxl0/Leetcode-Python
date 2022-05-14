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
                    ans += 1
                if sum3 > target:
                    k -= 1
                else:
                    j += 1
        return ans


if __name__ == "__main__":
    s = Solution()
    nums = [-2, 0, 1, 3]
    target = 2
    res = s.threeSumSmaller(nums, target)
    print(res)
