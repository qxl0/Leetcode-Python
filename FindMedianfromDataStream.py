class MedianFinder:
  
    def __init__(self):
       pass 

    def addNum(self, num: int) -> None:
       pass 

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
    res = s.findMedian()
    s.addNum(3)
    res = s.findMedian()
    print(res)