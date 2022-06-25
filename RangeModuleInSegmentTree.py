class SegmentTreeNode:
    def __init__(self, start, end, tracked):
        self.start = start
        self.end = end
        self.tracked = tracked
        # children needs update, in a lazy way
        self.childrenUpdate = 0
        self.left = self.right = None

    def __repr__(self) -> str:
        return f"tracked:{self.tracked},start:{self.start},end:{self.end}, {self.left},{self.right}"


# lazy tag
class SegmentTree:
    root = None

    # no interval tracked at begening
    def __init__(self, start, end):
        # lazy build
        self.root = SegmentTreeNode(start, end, False)

    def __repr__(self):
        return self.root.__repr__()

    def addRange(self, start, end):
        # [start, end)
        self._addRange(self.root, start, end - 1)

    def _addRange(self, node, start, end):
        if start == node.start and end == node.end:
            node.tracked = True
            node.childrenUpdate = 1
            return
        self._updateChildren(node)

        mid = node.start + (node.end - node.start) // 2

        # [start, end] overlap with [node.start, mid]
        if start <= mid:
            self._addRange(node.left, start, min(mid, end))
        # [start, end] overlap with
        if end > mid:
            self._addRange(node.right, max(start, mid + 1), end)

        node.tracked = node.left.tracked & node.right.tracked

    def _updateChildren(self, node):
        mid = node.start + (node.end - node.start) // 2

        if not node.left and not node.right:
            node.left = SegmentTreeNode(node.start, mid, node.tracked)
            node.right = SegmentTreeNode(mid + 1, node.end, node.tracked)
        elif node.childrenUpdate != 0:
            # Not actual implement
            # mark left if need update
            node.left.tracked = True if node.childrenUpdate == 1 else False
            node.left.childrenUpdate = node.childrenUpdate
            # right
            node.right.tracked = True if node.childrenUpdate == 1 else False
            node.right.childrenUpdate = node.childrenUpdate
        # done update
        node.childrenUpdate = 0

    def removeRange(self, start, end):
        self._removeRange(self.root, start, end)

    def _removeRange(self, node, start, end):
        if start == node.start and end == node.end:
            node.tracked = False
            node.childrenUpdate = -1
            return
        self._updateChildren(node)

        mid = node.start + (node.end - node.start) // 2

        # [start, end] overlap with [node.start, mid]
        if start <= mid:
            self._removeRange(node.left, start, min(mid, end))
        # [start, end] overlap with
        if end > mid:
            self._removeRange(node.right, max(start, mid + 1), end)

        node.tracked = node.left.tracked & node.right.tracked

    def queryRange(self, start, end):
        return self._queryRange(self.root, start, end - 1)

    def _queryRange(self, node, start, end):
        if start == node.start and end == node.end:
            return node.tracked
        self._updateChildren(node)

        result = True
        mid = node.start + (node.end - node.start) // 2

        # [start, end] overlap with [node.start, mid]
        if start <= mid:
            result &= self._queryRange(node.left, start, min(mid, end))
        # [start, end] overlap with
        if end > mid:
            result &= self._queryRange(node.right, max(start, mid + 1), end)

        return result


class RangeModule:
    def __init__(self):
        self.segTree = SegmentTree(0, 10**9)

    def addRange(self, left: int, right: int) -> None:
        self.segTree.addRange(left, right)

    def queryRange(self, left: int, right: int) -> bool:
        return self.segTree.queryRange(left, right)

    def removeRange(self, left: int, right: int) -> None:
        self.segTree.removeRange(left, right)


if __name__ == "__main__":
    sol = RangeModule()
    sol.addRange(10, 20)
    sol.removeRange(14, 16)
    sol.addRange(20, 21)
    res = sol.queryRange(10, 14)
    print("res is : ", res)
    res = sol.queryRange(13, 15)
    print("res is : ", res)
    res = sol.queryRange(16, 17)
    print("res is: ", res)
