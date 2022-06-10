from bisect import bisect_left, bisect_right
from operator import itemgetter


class CountIntervals:
    def __init__(self):
        self.intervals = []
        self.cur_count = 0

    def add(self, left: int, right: int) -> None:
        if not self.intervals:
            self.intervals.append([left, right])
            self.cur_count = right - left + 1
            return

        l = bisect_left(self.intervals, left, key=itemgetter(1))
        r = bisect_right(self.intervals, right, key=itemgetter(0))

        if l < len(self.intervals):
            left = min(left, self.intervals[l][0])

        if r > 0:
            right = max(right, self.intervals[r - 1][1])

        to_add = right - left + 1

        to_remove = 0
        for i in range(l, r):
            to_remove += self.intervals[i][1] - self.intervals[i][0] + 1

        self.cur_count += to_add - to_remove

        # TOO SLOW!!
        # 15 seconds!!
        # self.intervals = self.intervals[:l] + [[left, right]] + self.intervals[r:]

        # 1.3 - 1.6 seconds
        self.intervals[l:r] = [[left, right]]

    def count(self) -> int:
        return self.cur_count


if __name__ == "__main__":
    sol = CountIntervals()
    sol.add(1, 3)
    sol.add(3, 5)
    sol.add(2, 4)
    res = sol.count()
    print(res)
