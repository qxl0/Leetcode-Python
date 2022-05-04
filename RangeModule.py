"""
715. Range Module
Hard

928

72

Add to List

Share
A Range Module is a module that tracks ranges of numbers. Design a data structure to track the ranges represented as half-open intervals and query about them.

A half-open interval [left, right) denotes all the real numbers x where left <= x < right.

Implement the RangeModule class:

RangeModule() Initializes the object of the data structure.
void addRange(int left, int right) Adds the half-open interval [left, right), tracking every real number in that interval. Adding an interval that partially overlaps with currently tracked numbers should add any numbers in the interval [left, right) that are not already tracked.
boolean queryRange(int left, int right) Returns true if every real number in the interval [left, right) is currently being tracked, and false otherwise.
void removeRange(int left, int right) Stops tracking every real number currently being tracked in the half-open interval [left, right).
"""


from audioop import add
from unittest import removeResult


class RangeModule:
    def __init__(self):
        self.intervals = []

    def isearlier(self, a, b):
        return a[1] < b[0]

    def issame(self, a, b):
        return a[0] == b[0] and a[1] == b[1]

    def addRange(self, left: int, right: int) -> None:
        # insert
        output = []
        newInterval = [left, right]
        for interval in self.intervals:
            if self.isearlier(interval, newInterval):
                output.append(interval)
            elif self.isearlier(newInterval, interval):
                output.append(newInterval)
                newInterval = interval
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
        output.append(newInterval)
        self.intervals = output

    def queryRange(self, left: int, right: int) -> bool:
        queryinterval = [left, right]
        for interval in self.intervals:
            if self.issame(queryinterval, interval):
                return True
            elif self.isearlier(queryinterval, interval):
                return False
            elif self.isearlier(interval, queryinterval):
                continue
            else:
                # check
                if (
                    interval[0] < queryinterval[0] < interval[1]
                    and queryinterval[1] > interval[1]
                ):
                    return False
                elif (
                    queryinterval[0] < interval[0] < queryinterval[1]
                    and interval[1] > queryinterval[1]
                ):
                    return False
                elif (
                    interval[0] <= queryinterval[0] <= interval[1]
                    and queryinterval[1] <= interval[1]
                ):
                    return True
        return False

    def removeRange(self, left: int, right: int) -> None:
        queryinterval = [left, right]
        for i, interval in enumerate(self.intervals):
            if self.isearlier(queryinterval, interval):
                return
            elif self.isearlier(interval, queryinterval):
                continue
            else:
                if (
                    interval[0] < queryinterval[0] < interval[1]
                    and queryinterval[1] > interval[1]
                ):
                    interval[1] = queryinterval[0]
                elif (
                    queryinterval[0] < interval[0] < queryinterval[1]
                    and interval[1] > queryinterval[1]
                ):
                    interval[0] = queryinterval[1]
                elif (
                    interval[0] < queryinterval[0] < interval[1]
                    and interval[0] < queryinterval[1] < interval[1]
                ):
                    self.intervals.insert(i + 1, [queryinterval[1], interval[1]])
                    interval[1] = queryinterval[0]
                elif (
                    queryinterval[0] <= interval[0] < queryinterval[1]
                    and queryinterval[0] < interval[1] <= queryinterval[1]
                ):
                    self.intervals.remove(interval)


class RangeModule2:
    def __init__(self):
        self.ranges = []

    def touching_ranges(self, left, right):
        """find all the ranges that touch interval [left, right]"""
        i, j = 0, len(self.ranges) - 1
        step = len(self.ranges) // 2
        while step >= 1:
            while i + step < len(self.ranges) and self.ranges[i + step - 1][1] < left:
                i += step
            while j - step >= 0 and self.ranges[j - step + 1][0] > right:
                j -= step
            step //= 2
        return i, j

    def addRange(self, left: int, right: int) -> None:
        if not self.ranges or self.ranges[-1][1] < left:
            self.ranges.append((left, right))
            return
        if self.ranges[0][0] > right:
            self.ranges.insert(0, (left, right))
            return
        i, j = self.touching_ranges(left, right)
        self.ranges[i : j + 1] = [
            (min(self.ranges[i][0], left), max(self.ranges[j][1], right))
        ]

    def queryRange(self, left: int, right: int) -> bool:
        if not self.ranges:
            return False
        i, j = self.touching_ranges(left, right)
        return self.ranges[i][0] <= left and right <= self.ranges[i][1]

    def removeRange(self, left: int, right: int) -> None:
        if not self.ranges or self.ranges[0][0] > right or self.ranges[-1][1] < left:
            return
        i, j = self.touching_ranges(left, right)
        new_ranges = []
        for k in range(i, j + 1):
            if self.ranges[k][0] < left:
                new_ranges.append((self.ranges[k][0], left))
            if self.ranges[k][1] > right:
                new_ranges.append((right, self.ranges[k][1]))
        self.ranges[i : j + 1] = new_ranges


if __name__ == "__main__":
    sol = RangeModule()
    # sol.addRange(10, 20)
    # sol.removeRange(14, 16)
    # res = sol.queryRange(10, 14)
    # print("res is : ", res)
    # res = sol.queryRange(13, 15)
    # print("res is : ", res)
    # res = sol.queryRange(16, 17)
    sol.addRange(55, 62)
    sol.addRange(1, 29)
    sol.removeRange(18, 49)
    sol.removeRange(40, 45)
    sol.removeRange(4, 58)
    sol.removeRange(57, 69)
    sol.removeRange(20, 30)
    sol.removeRange(1, 40)
    sol.removeRange(32, 93)
    sol.addRange(38, 100)
    sol.removeRange(50, 64)
    sol.addRange(26, 72)

    sol.addRange(44, 85)
    sol.addRange(10, 71)
    res = sol.queryRange(54, 70)
    print("res is: ", res)
