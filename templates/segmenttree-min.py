import sys


class SegmentTreeNode:
    def __init__(self, start, end, minnum):
        self.start = start
        self.end = end
        self.minnum = minnum
        self.left = self.right = None


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
