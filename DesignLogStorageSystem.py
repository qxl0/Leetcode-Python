from collections import Counter
import heapq
from math import inf
from typing import List


class LogSystem:
    def __init__(self):
        self.logs = []

    def put(self, id: int, timestamp: str) -> None:
        ts = self.convert(timestamp)
        self.logs.append((ts, id))

    def convert(self, timestamp):
        lst = timestamp.split(":")
        lst2 = map(int, lst)
        return self.convert2(lst2)

    def convert2(self, lst):
        yy, mm, dd, hh, mt, ss = lst
        # ret = yy*(12*31)*24*60*60+mm*31*24*60*60+dd*24*60*60+hh*60*60+mm*60+ss
        ret = (yy, mm, dd, hh, mt, ss)
        return ret

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        ans = []
        start_s = self.convertExt(start, granularity, False)
        end_s = self.convertExt(end, granularity, True)

        for i in range(len(self.logs)):
            ts, id = self.logs[i]
            if start_s <= ts <= end_s:
                ans.append(id)
        return ans

    def convertExt(self, ts, gy, end):
        h = {"Year": 0, "Month": 1, "Day": 2, "Hour": 3, "Minute": 4, "Second": 5}
        tslist = ts.split(":")
        res = ["0000", "00", "00", "00", "00", "00"]
        for i in range(h[gy] + 1):
            res[i] = tslist[i]
        t = list(map(int, res))
        if end:
            t[h[gy]] += 1
        return self.convert2(t)


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)


if __name__ == "__main__":
    sol = LogSystem()
    # [1,"2017:01:01:23:59:59"],[2,"2017:01:02:23:59:59"],["2017:01:01:23:59:58","2017:01:02:23:59:58","Second"]]
    sol.put(1, "2017:01:01:23:59:59")
    sol.put(2, "2017:01:02:23:59:59")
    res = sol.retrieve("2017:01:01:23:59:58", "2017:01:02:23:59:58", "Second")
    print(res)
