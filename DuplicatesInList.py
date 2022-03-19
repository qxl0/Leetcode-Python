class Solution:
    def duplicates(self, nums):
        return len(nums) != len(set(nums))


if __name__ == "__main__":
    s = Solution()
    nums = [1, 2, 4, 2]
    res = s.duplicates(nums)
    print(res)
