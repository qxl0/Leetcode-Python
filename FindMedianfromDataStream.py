"""
295. Find Median from Data Stream

The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
"""
from heapq import *
from lib2to3.pgen2.token import MINEQUAL


class MedianFinder:
    def __init__(self):
        self.minq = []
        self.maxq = []

    def addNum(self, num: int) -> None:
        heappush(self.maxq, -num)
        heappush(self.minq, -heappop(self.maxq))

        if len(self.maxq) < len(self.minq):
            heappush(self.maxq, -heappop(self.minq))

    def findMedian(self) -> float:
        if len(self.minq) == len(self.maxq):
            return (self.minq[0] + -self.maxq[0]) / 2
        else:
            return -self.maxq[0]


class MedianFinder2:
    def __init__(self):
        self.heaps = None, [], []
        self.i = 1

    def addNum(self, num):
        heappush(self.heaps[-self.i], -heappushpop(self.heaps[self.i], num * self.i))
        self.i *= -1

    def findMedian(self):
        return (self.heaps[self.i][0] * self.i - self.heaps[-1][0]) / 2.0


class MedianFinder3:
    def __init__(self):
        self.data = 1, [], []

    def addNum(self, num):
        sign, h1, h2 = self.data
        heappush(h2, -heappushpop(h1, num * sign))
        self.data = -sign, h2, h1

    def findMedian(self):
        sign, h1, h2 = d = self.data
        return (h1[0] * sign - d[-sign][0]) / 2.0


class MedianFinder4:
    def __init__(s):
        h = [[], 1, -1, i := []]
        s.addNum = (
            lambda n: heappush(h[-1], -heappushpop(h[0], n * h[1])) or h.reverse()
        )
        s.findMedian = lambda: (h[0][0] * h[1] - i[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

if __name__ == "__main__":
    s = MedianFinder()
    # s = MedianFinder3()

    s.addNum(7)
    s.addNum(2)
    s.addNum(20)
    s.addNum(5)
    # s.addNum(4)
    res = s.findMedian()
    s.addNum(23)
    s.addNum(26)
    res = s.findMedian()
    print(res)
