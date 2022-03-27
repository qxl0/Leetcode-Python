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
        if len(self.minq) == len(self.maxq):
            return (self.minq[0] + -self.maxq[0]) / 2
        else:
            return -self.maxq[0]


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
