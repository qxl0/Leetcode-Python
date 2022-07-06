from collections import defaultdict
from typing import List


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0

        stop2bus = defaultdict(list)
        for bus, stops in enumerate(routes):
            for stop in stops:
                stop2bus[stop].append(bus)
        adj = defaultdict(list)
        for bus, stops in enumerate(routes):
            for stop in stops:
                for nb in stop2bus[stop]:
                    if nb == bus:
                        continue
                    adj[bus].append(nb)

        q = []
        for bus in stop2bus[S]:
            q.append((bus, 1))
        Tbus = stop2bus[T]
        while q:
            cb, step = q.pop(0)
            if cb in Tbus:
                return step
            for nb in adj[cb]:
                q.append((nb, step + 1))
        return -1


if __name__ == "__main__":
    sol = Solution()
    routes = [[1, 2, 7], [3, 6, 7]]
    S = 1
    T = 6
    res = sol.numBusesToDestination(routes, S, T)
    print("Ans is: ", res)
