class SegmentTreeNode:
    def __init__(self, start, end, count):
        self.start = start
        self.end = end
        self.count = count  # count less than given integer in array
        self.left = self.right = None


class SegmentTree:
    root = None

    def __init__(self, length):
        self.root = self.buildHelper(0, length - 1)

    def buildHelper(self, start, end):
        if start > end:
            return None
        if start == end:
            return SegmentTreeNode(start, end, 0)

        node = SegmentTreeNode(start, end, 0)
        mid = start + (end - start) // 2
        node.left = self.buildHelper(start, mid)
        node.right = self.buildHelper(mid + 1, end)

        # maintain count
        if node.left:
            node.count += node.left.count
        if node.right:
            node.count += node.right.count

        return node

    def queryCount(self, start, end):
        return self._queryCount(self.root, start, end)

    def _queryCount(self, node, start, end):
        # print(start,end)
        if node == None or start > end:
            return 0
        if start <= node.start and node.end <= end:
            return node.count

        mid = node.start + (node.end - node.start) // 2

        leftRet = 0
        rightRet = 0

        if start <= mid:
            leftRet = self._queryCount(node.left, start, end)
        if mid + 1 <= end:
            rightRet = self._queryCount(node.right, start, end)
        # print('return:', leftRet+rightRet)
        return leftRet + rightRet

    # nums[index] += value
    # Note: nums can have duplicates
    def modify(self, index, value):
        self._modify(self.root, index, value)

    def _modify(self, node, index, value):
        if node.start == node.end and node.start == index:
            node.count += value
            return
        mid = node.start + (node.end - node.start) // 2
        if index <= mid:
            self._modify(node.left, index, value)
        else:
            self._modify(node.right, index, value)

        node.count = node.left.count + node.right.count
        return


if __name__ == "__main__":
    nums = [1, 2, 7, 8, 5]
    s = SegmentTree(10000)
    queries = [1, 8, 5]
    ans = []

    root = SegmentTree(10001)
    for num in nums:
        root.modify(num, 1)

    for i in queries:
        ans.append(root.queryCount(0, i - 1))  # <i
    print(ans)
