import heapq
from lib2to3.pgen2.token import MINEQUAL


class MedianFinder:
    def __init__(self):
        self.minq = []
        self.maxq = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxq, -num)
        heapq.heappush(self.minq, -heapq.heappop(self.maxq))

        if len(self.maxq) < len(self.minq):
            heapq.heappush(self.maxq, -heapq.heappop(self.minq))

    def findMedian(self) -> float:
        pass


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

if __name__ == "__main__":
    s = MedianFinder()

    s.addNum(1)
    s.addNum(2)
    s.addNum(20)
    s.addNum(12)
    s.addNum(4)
    res = s.findMedian()
    s.addNum(3)
    res = s.findMedian()
    print(res)
