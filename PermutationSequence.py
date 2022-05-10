"""
60. Permutation Sequence
Hard

3536

391

Add to List

Share
The set [1, 2, 3, ..., n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.
"""


from math import factorial
from typing import List


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        res, nums = "", [i for i in range(1, n + 1)]
        k -= 1
        while n:
            n -= 1
            index, k = divmod(k, factorial(n))
            res += str(nums.pop(index))
        return res

    def getPermutation2(self, n, k):
        nums = [i for i in range(1, n + 1)]
        k -= 1

        def helper(n, k):
            if n == 1 and k == 0:
                return str(nums.pop())
            n -= 1
            index, k = divmod(k, factorial(n))
            return str(nums.pop(index)) + helper(n, k)

        return helper(n, k)


class Solution2:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [str(i) for i in range(1, n + 1)]
        facnum = []
        i = 1
        total = k - 1
        while total:
            total, f = divmod(total, i)
            facnum.append(f)
            i += 1
        # len(facnum) == n
        i = len(facnum)
        while i < n:
            facnum.append(0)
            i += 1
        # got the facnum
        output = []
        for n in facnum[::-1]:
            output.append(nums[n])
            nums.remove(nums[n])
        return "".join(output)


if __name__ == "__main__":
    sol = Solution2()
    # n = 3
    # k = 3
    # n = 4
    # k = 9
    n = 3
    k = 3
    res = sol.getPermutation(n, k)
    print(res)
