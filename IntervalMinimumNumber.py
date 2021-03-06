import sys
from typing import (
    List,
)

# from lintcode import (
#     Interval,
# )

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class SegmentTreeNode:
    def __init__(self, start, end, minnum):
        self.start = start
        self.end = end
        self.minnum = minnum
        self.left = self.right = None

    def __repr__(self) -> str:
        return f"min: {self.minnum}, left:{self.left}, right: {self.right}"


class SegmentTree:
    root = None

    def __init__(self, nums):
        self.root = self.buildHelper(0, len(nums) - 1, nums)

    def buildHelper(self, start, end, nums):
        if start > end:
            return None
        if start == end:
            return SegmentTreeNode(start, end, nums[start])
        # root has Child
        root = SegmentTreeNode(start, end, sys.maxsize)
        mid = start + (end - start) // 2
        root.left = self.buildHelper(start, mid, nums)
        root.right = self.buildHelper(mid + 1, end, nums)

        # minimum
        if root.left:
            root.minnum = min(root.minnum, root.left.minnum)
        if root.right:
            root.minnum = min(root.minnum, root.right.minnum)

        return root

    def queryMin(self, start, end):
        return self._queryMin(self.root, start, end)

    def _queryMin(self, node, start, end):
        if start <= node.start and node.end <= end:
            return node.minnum
        mid = node.start + (node.end - node.start) // 2
        leftRet = sys.maxsize
        rightRet = sys.maxsize
        if start <= mid:
            leftRet = self._queryMin(node.left, start, end)
        if mid < end:
            rightRet = self._queryMin(node.right, start, end)

        return min(leftRet, rightRet)


class Solution:
    """
    @param a: An integer array
    @param queries: An query list
    @return: The result list
    """

    def interval_min_number(self, a: List[int], queries) -> List[int]:
        # write your code here
        ans = []
        if not queries or len(queries) == 0:
            return ans
        segTree = SegmentTree(a)

        for query in queries:
            ans.append(segTree.queryMin(query[0], query[1]))

        return ans


if __name__ == "__main__":
    sol = Solution()
    # a = [4, 5, 7, 1]
    # queries = [(1, 2), (1, 3)]
    a = [2, 3, 1, 4, 5]
    queries = [(0, 0)]
    res = sol.interval_min_number(a, queries)
    print(res)
