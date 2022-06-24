import sys


class SegmentTreeNode:
    def __init__(self, start, end, min):
        self.start = start
        self.end = end
        self.min = min
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
            root.min = min(root.min, root.left.min)
        if root.right:
            root.min = min(root.min, root.right.min)

        return root

    def queryMin(self, start, end):
        return self._queryMin(self.root, start, end)

    def _queryMin(self, node, start, end):
        if start <= node.start and node.end <= end:
            return node.min
        mid = node.start + (node.end - node.start) // 2
        leftRet = sys.maxsize
        rightRet = sys.maxsize
        if start <= mid:
            leftRet = self._queryMin(node.left, start, end)
        if mid < end:
            rightRet = self._queryMin(node.right, start, end)

        return min(leftRet, rightRet)

    def modify(self, index, value):
        self._modify(self.root, index, value)

    def _modify(self, root: SegmentTreeNode, index: int, value: int):
        # write your code here
        if root.start == root.end and root.start == index:
            root.min = value
            return

        mid = root.start + (root.end - root.start) // 2

        # left root.start, mid
        if index <= mid:
            self._modify(root.left, index, value)
        else:
            self._modify(root.right, index, value)

        # maintain min
        root.min = min(root.left.min, root.right.min)
        return


if __name__ == "__main__":
    nums = [3, 2, 9, 4]
    s = SegmentTree(nums)
    res = s.queryMin(0, 1)
    print("Ans is: ", res)
    res = s.queryMin(2, 3)
    print("Ans is: ", res)
    s.modify(1, 1)
    res = s.queryMin(0, 3)
    print("after modify [0,3]: min=", res)
