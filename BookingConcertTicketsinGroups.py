class SegTreeNode:
    def __init__(self, arr):
        N = 100000
        self.n = len(arr)
        self.tree = [0] * (2 * N)
        for i in range(self.n):
            self.tree[self.n + i] = arr[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[i << 1] + self.tree[i << 1 | 1]

    def updateRange(self, idx, val):
        self.tree[idx + self.n] = val
        idx += self.n
        i = idx
        while i > 1:
            self.tree[i >> 1] = self.tree[i] + self.tree[i ^ 1]
            i >>= 1

    def queryRange(self, l, r):
        r += 1
        res = 0
        l += self.n
        r += self.n
        while l < r:
            if l & 1:
                res += self.tree[l]
                l += 1
            if r & 1:
                r -= 1
                res += self.tree[r]
            l >>= 1
            r >>= 1
        return res


class SegTreeNode2:
    def __init__(self, arr):
        N = 100000
        self.n = len(arr)
        self.tree = [0] * (2 * N)
        for i in range(self.n):
            self.tree[self.n + i] = arr[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = max(self.tree[i << 1], self.tree[i << 1 | 1])

    def updateRange(self, idx, val):
        self.tree[idx + self.n] = val
        idx += self.n
        i = idx
        while i > 1:
            self.tree[i >> 1] = max(self.tree[i], self.tree[i ^ 1])
            i >>= 1

    def queryRange(self, l, r):
        r += 1
        res = 0
        l += self.n
        r += self.n
        while l < r:
            if l & 1:
                res = max(res, self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                res = max(res, self.tree[r])
            l >>= 1
            r >>= 1
        return res


class BookMyShow:
    def __init__(self, n: int, m: int):
        self.seg = SegTreeNode2([m for _ in range(n)])
        self.regseg = SegTreeNode([m for _ in range(n)])
        self.c = m
        self.av = 0

    def gather(self, k: int, maxRow: int) -> List[int]:
        if self.seg.query(0, maxRow) < k:
            return []
        op, ed = 0, maxRow
        res = float("inf")
        while op <= ed:
            m = (op + ed) // 2
            temp = self.seg.query(op, m)
            if temp >= k:
                res = min(res, m)
                ed = m - 1
            else:
                op = m + 1
        prev = self.seg.query(res, res)
        ans = [res, self.c - prev]
        self.seg.update(res, prev - k)
        self.regseg.update(res, prev - k)
        if (not prev - k) and self.av == res:
            self.av += 1
        return ans

    def scatter(self, k: int, maxRow: int) -> bool:
        if self.regseg.query(0, maxRow) < k:
            return False
        while k:
            temp = self.regseg.query(self.av, self.av)
            if k - temp <= 0:
                self.seg.update(self.av, temp - k)
                self.regseg.update(self.av, temp - k)
                break
            else:
                k -= temp
                self.seg.update(self.av, 0)
                self.regseg.update(self.av, 0)
            self.av += 1
        return True
