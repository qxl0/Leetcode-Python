class SegTreeNode:
    def __init__(self, a, b, val):  # init [a,b] with val
        self.tag = 0
        self.start = a
        self.end = b
        self.left = self.right = None
        if a == b:
            self.info = val
            return
        mid = (a + b) // 2
        if not self.left:
            self.left = SegTreeNode(a, mid, val)
            self.right = SegTreeNode(mid + 1, b, val)
            self.info = self.left.info + self.right.info

    def pushDown(self):
        if self.tag == 1 and self.left:
            self.left.info = self.info
            self.right.info = self.info
            self.left.tag = 1
            self.right.tag = 1
            self.tag = 0

    def updateRange(self, a, b, val):  # set range [a,b] with val
        if b < self.start or self.end < a:
            return
        if a <= self.start and self.end <= b:
            self.info = val * (self.end - self.start + 1)
            self.tag = 1
            return

        if self.left:
            self.pushDown()
            self.left.updateRange(a, b, val)
            self.right.updateRange(a, b, val)
            self.info = self.left.info + self.right.info

    def queryRange(self, a, b):  # query sum over [a,b]
        if b < self.start or a > self.end:
            return 0
        if a <= self.start and self.end <= b:
            return self.info

        if self.left:
            self.pushDown()
            ret = self.left.queryRange(a, b) + self.right.queryRange(a, b)
            self.info = self.left.info + self.right.info
            return ret


if __name__ == "__main__":
    length = 8
    val = 1
    updates = [[0, 3, 3], [4, 7, 9]]
    queries = [[0, 3], [2, 5]]
    sol = SegTreeNode(0, length - 1, val)
    for s, e, val in updates:
        sol.updateRange(s, e, val)
    for s, e in queries:
        res = sol.queryRange(s, e)
        print(res)
