"""
"""


from bisect import bisect
from typing import List


class Solution:
    def maxSumSubmatrix(self, matrix, k):
        def maxSumSublist(vals):
            maxSum = float("-inf")
            prefixSum = 0
            prefixSums = [float("inf")]
            for val in vals:
                bisect.insort(prefixSums, prefixSum)
                prefixSum += val
                i = bisect.bisect_left(prefixSums, prefixSum - k)
                maxSum = max(maxSum, prefixSum - prefixSums[i])
            return maxSum

        maxSum = float("-inf")
        columns = zip(*matrix)
        for left in range(len(columns)):
            rowSums = [0] * len(matrix)
            for column in columns[left:]:
                rowSums = map(int.__add__, rowSums, column)
                maxSum = max(maxSum, maxSumSublist(rowSums))
        return maxSum


if __name__ == "__main__":
    sol = Solution()
    matrix = [[1, 0, 1], [0, -2, 3]]
    k = 2
    res = sol.maxSumSubmatrix(matrix, k)
    print(i, start, res)
