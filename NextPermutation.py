"""
31. Next Permutation
Medium

9363

3149

Add to List

Share
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are considered permutations of arr: [1,2,3], [1,3,2], [3,1,2], [2,3,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.
"""


from typing import List


class Solution:
    """
    @param s: a string
    @return: return a string
    """

    def nextPermutation(self, nums: List[int]) -> None:
        def reverse(arr, l, r):
            # in place reverse
            while l < r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1

        n = len(nums)
        for k in range(n - 2, -1, -1):
            if nums[k] < nums[k + 1]:
                break
        if k <= 0:
            reverse(nums, 0, n - 1)
        else:
            for l in range(n - 1, k, -1):
                if nums[l] > nums[k]:
                    break
            nums[k], nums[l] = nums[l], nums[k]
            reverse(nums, k + 1, n - 1)


if __name__ == "__main__":

    sol = Solution()
    # nums = [1, 1, 3]
    # nums = [1, 2, 3]
    # nums = [3, 1, 2]
    # nums = [2, 3, 1]
    # nums = [2, 3, 6, 5, 4, 1, 0]
    nums = [3, 2, 1]
    sol.nextPermutation(nums)
    print(nums)
