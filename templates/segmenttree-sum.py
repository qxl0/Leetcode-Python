class SegmentTreeNode:
    def __init__(self, start, end, sum):
        self.start = start
        self.end = end
        self.sum = sum
        self.left = self.right = None

    def __repr__(self) -> str:
        return f"sum:{self.sum},start:{self.start},end:{self.end}"


class SegmentTree:
    root = None

    def __init__(self, nums):
        self.root = self.buildHelper(0, len(nums) - 1, nums)

    def buildHelper(self, start, end, nums):
        if start > end:
            return None
        if start == end:
            return SegmentTreeNode(start, end, nums[start])

        node = SegmentTreeNode(start, end, 0)
        mid = start + (end - start) // 2
        node.left = self.buildHelper(start, mid, nums)
        node.right = self.buildHelper(mid + 1, end, nums)

        # maintain
        if node.left:
            node.sum += node.left.sum
        if node.right:
            node.sum += node.right.sum

        return node

    def querySum(self, start, end):
        return self._querySum(self.root, start, end)

    def _querySum(self, node, start, end):
        if start <= node.start and node.end <= end:
            return node.sum
        mid = node.start + (node.end - node.start) // 2

        leftRet = 0
        rightRet = 0

        if start <= mid:
            leftRet = self._querySum(node.left, start, end)
        if mid + 1 <= end:
            rightRet = self._querySum(node.right, start, end)
        return leftRet + rightRet

    def modify(self, index, value):
        self._modify(self.root, index, value)

    def _modify(self, node, index, value):
        if node.start == node.end and node.start == index:
            node.sum = value
            return
        mid = node.start + (node.end - node.start) // 2
        if index <= mid:
            self._modify(node.left, index, value)
        else:
            self._modify(node.right, index, value)
        node.sum = node.left.sum + node.right.sum
        return


if __name__ == "__main__":
    nums = [1, 2, 7, 8, 5]
    s = SegmentTree(nums)
    res = s.querySum(0, 2)
    print("Ans is: ", res)
    res = s.querySum(2, 3)
    print("Ans is: ", res)
    s.modify(1, 5)
    res = s.querySum(0, 1)
    print("after modify: ", res)
