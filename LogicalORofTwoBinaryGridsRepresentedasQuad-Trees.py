class Node:
    def __init__(
        self,
        val,
        isLeaf,
        topLeft=None,
        topRight=None,
        bottomLeft=None,
        bottomRight=None,
    ):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def intersect(self, quadTree1: "Node", quadTree2: "Node") -> "Node":
        if not quadTree1 or not quadTree2:
            return quadTree1 if quadTree1 else quadTree2

        if quadTree1.isLeaf or quadTree2.isLeaf:
            if (
                quadTree1.isLeaf
                and quadTree2.isLeaf
                or (quadTree1.isLeaf and quadTree1.val)
                or (quadTree2.isLeaf and quadTree2.val)
            ):
                newval = quadTree1.val or quadTree2.val
                return Node(newval, True, None, None, None, None)

        res = Node()
        res.isLeaf = False
        res.topLeft = self.intersect(quadTree1.topLeft, quadTree2.topLeft)
        res.topRight = self.intersect(quadTree1.topRight, quadTree2.topRight)
        res.bottomLeft = self.intersect(quadTree1.bottomLeft, quadTree2.bottomLeft)
        res.bottomRight = self.intersect(quadTree1.bottomRight, quadTree2.bottomRight)

        isLeaf = self.handleAll(
            res.topLeft.isLeaf,
            res.topRight.isLeaf,
            res.bottomLeft.isLeaf,
            res.bottomRight.isLeaf,
        )
        val = self.handleAll(
            res.topLeft.val, res.topRight.val, res.bottomLeft.val, res.bottomRight.val
        )

        if isLeaf == 4 and (val == 4 or val == 0):
            res.isLeaf = True
            res.val = True if val == 4 else False
            res.topLeft = res.topRight = res.bottomLeft = res.bottomRight = None
            return res

        return res

    def handleAll(self, a, b, c, d):
        i1 = 1 if a else 0
        i2 = 1 if b else 0
        i3 = 1 if c else 0
        i4 = 1 if d else 0

        return i1 + i2 + i3 + i4


if __name__ == "__main__":
    sol = Solution()
    t1 = Node(0, False)
    res = sol.intersect(t1, t2)

    print(res)
