"""
128. Longest Consecutive Sequence
Medium

8747

386

Add to List

Share
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
"""
import collections
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        num_set = set(nums)
        for num in nums:
            cur_len, j = 1, 1
            while num - j in num_set:
                num_set.remove(num - j)
                cur_len, j = cur_len + 1, j + 1
            j = 1
            while num + j in num_set:
                num_set.remove(num + j)
                cur_len, j = cur_len + 1, j + 1
            longest = max(longest, cur_len)
        return longest

    def longestConsecutive2(self, nums: List[int]) -> int:
        longest, S = 0, set(nums)
        for num in S:
            if num - 1 in S:
                continue
            count = 1
            while num + count in S:
                count += 1
            longest = max(longest, count)
        return longest


if __name__ == "__main__":
    sol = Solution()
    # nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    nums = [100, 4, 200, 1, 3, 2]
    res = sol.longestConsecutive2(nums)
    print("result is: ", res)
