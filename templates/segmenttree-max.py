import sys


class SegmentTreeNode:
    def __init__(self, start, end, max=-sys.maxsize):
        self.start = start
        self.end = end
        self.max = max
        self.left = self.right = None

    def __repr__(self) -> str:
        return f"max:{self.max},start:{self.start},end:{self.end}, {self.left},{self.right}"


class SegmentTree:
    root = None

    def __init__(self, nums):
        self.root = self.buildHelper(0, len(nums) - 1, nums)

    def __repr__(self):
        return self.root

    def buildHelper(self, start, end, nums):
        if start > end:
            return None
        if start == end:
            return SegmentTreeNode(start, end, nums[start])
        # root has Child
        root = SegmentTreeNode(start, end)
        mid = start + (end - start) // 2
        root.left = self.buildHelper(start, mid, nums)
        root.right = self.buildHelper(mid + 1, end, nums)

        # maximum
        if root.left:
            root.max = max(root.max, root.left.max)
        if root.right:
            root.max = max(root.max, root.right.max)

        return root

    def queryMax(self, start, end):
        return self._queryMax(self.root, start, end)

    def _queryMax(self, node, start, end):
        if start <= node.start and node.end <= end:
            return node.max
        mid = node.start + (node.end - node.start) // 2
        leftRet = -sys.maxsize
        rightRet = -sys.maxsize
        if start <= mid:
            leftRet = self._queryMax(node.left, start, end)
        if mid < end:
            rightRet = self._queryMax(node.right, start, end)

        return max(leftRet, rightRet)

    def modify(self, index, value):
        self._modify(self.root, index, value)

    def _modify(self, root: SegmentTreeNode, index: int, value: int):
        # exit
        if root.start == root.end and root.start == index:
            root.max = value
            return

        mid = root.start + (root.end - root.start) // 2

        # left root.start, mid
        if index <= mid:
            self._modify(root.left, index, value)
        else:
            self._modify(root.right, index, value)

        # maintain max
        root.max = max(root.left.max, root.right.max)
        return


if __name__ == "__main__":
    nums = [3, 2, 1, 4]
    s = SegmentTree(nums)
    res = s.queryMax(0, 1)
    print("Ans is: ", res)
    res = s.queryMax(2, 3)
    print("Ans is: ", res)
    s.modify(1, 5)
    res = s.queryMax(0, 1)
    print("after modify: ", res)
