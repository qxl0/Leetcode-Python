"""
759. Employee Free Time
Hard

1398

87

Add to List

Share
We are given a list schedule of employees, which represents the working time for each employee.

Each employee has a list of non-overlapping Intervals, and these intervals are in sorted order.

Return the list of finite intervals representing common, positive-length free time for all employees, also in sorted order.

(Even though we are representing Intervals in the form [x, y], the objects inside are Intervals, not lists or arrays. For example, schedule[0][0].start = 1, schedule[0][0].end = 2, and schedule[0][0][0] is not defined).  Also, we wouldn't include intervals like [5, 5] in our answer, as they have zero length.
"""


from math import floor
from typing import List


class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end


class Solution:
    def employeeFreeTime(self, schedule):
        diff = {}
        for employee in schedule:
            for interval in employee:
                start, end = interval
                diff[start] = diff.get(start, 0) + 1
                diff[end] = diff.get(end, 0) - 1
        sum = 0
        ans = []
        start = -1
        end = -1
        for time, event in diff:
            sum += event
            if sum == 0:
                start = time
            elif start >= 0 and sum >= 1:
                ans.append([start, end])
                start, end = -1, -1
        return ans


if __name__ == "__main__":
    sol = Solution()
    schedule = [[[1, 2], [5, 6]], [[1, 3]], [[4, 10]]]
    res = sol.employeeFreeTime(schedule)

    print(res)
