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


from typing import List


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        pass


if __name__ == "__main__":
    sol = Solution()
    n = 3
    k = 3
    res = sol.getPermutation(n, k)
    print(res)
