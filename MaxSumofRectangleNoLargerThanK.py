"""
"""


from bisect import bisect
from typing import List


class Solution:
    class Solution(object):
        def maxSumSubmatrix(self, matrix, k):
            """
            :type matrix: List[List[int]]
            :type k: int
            :rtype: int
            """
            # O(MlogM) method is called only when quick check is passed,
            # which should only be used when max sum > k and try to use ceiling to find a sum <= k
            def bstSearch(sum_list, k):
                currSum = 0
                bst = BST()
                bst.insert(0)
                for sum in sum_list:
                    currSum += sum
                    prevSum = bst.ceiling(currSum - k)
                    self.maxSum = max(self.maxSum, currSum - prevSum)
                    bst.insert(currSum)

            # O(M) method is called for quick check the max sum of any sub arrays
            def kadane(sum_list, k):
                maxSum = -(1 << 31)
                currSum = 0
                for sum in sum_list:
                    currSum = max(sum, sum + currSum)
                    maxSum = max(maxSum, currSum)
                if maxSum <= k:
                    self.maxSum = max(self.maxSum, maxSum)
                    return False
                else:
                    return True

            M = len(matrix)
            if M == 0:
                return 0
            N = len(matrix[0])
            if N == 0:
                return 0

            self.maxSum = -(1 << 31)
            for left in range(N):
                sum_list = [0] * M
                for right in range(left, N):
                    for i in range(M):
                        sum_list[i] += matrix[i][right]

                    # O(M) method kadane is called for quick check
                    # False means the max sum in any sub array <= k, so unnecessary to do bstSearch,
                    # which should only be used when max sum > k and try to use ceiling to find a sum <= k
                    if kadane(sum_list, k):
                        bstSearch(sum_list, k)

                    # early temination condition
                    if self.maxSum == k:
                        return k

            return self.maxSum


class BST:
    def __init__(self):
        self.root = {}

    def insert(self, value):
        if self.root:
            self._insert(self.root, value)
        else:
            self.root = {"value": value}

    def _insert(self, cur_node, value):
        if value < cur_node["value"]:
            if "left" in cur_node:
                self._insert(cur_node["left"], value)
            else:
                cur_node["left"] = {"value": value}
        else:
            if "right" in cur_node:
                self._insert(cur_node["right"], value)
            else:
                cur_node["right"] = {"value": value}

    def ceiling(self, value):
        cur_node = self.root
        result = 1 << 31
        while cur_node:
            if cur_node["value"] < value:
                cur_node = cur_node.get("right", None)
            else:
                result = min(result, cur_node["value"])
                cur_node = cur_node.get("left", None)
        return result


if __name__ == "__main__":
    sol = Solution()
    matrix = [[1, 0, 1], [0, -2, 3]]
    k = 2
    res = sol.maxSumSubmatrix(matrix, k)
    print(res)
