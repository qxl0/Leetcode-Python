"""
268. Missing Number
Easy

5316

2830

Add to List

Share
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
"""


from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        s = sum(nums)

        totalShouldBe = n * (n + 1) / 2

        return int(totalShouldBe - s)

    def print_bits(self, x):
        lst = []
        original = x
        while x:
            tmp = x & 1
            lst.append(tmp)
            x >>= 1
        while len(lst) < 32:
            lst.append(0)
        lst = lst[::-1]
        res = " ".join(str(e) for e in lst)
        print(res)


if __name__ == "__main__":
    sol = Solution()
    # nums = [3, 0, 1]
    nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    res = sol.missingNumber(nums)
    print("Ans is: ", res)
