import collections
import itertools
from typing import List


class Solution:
    def minNumberOfSemesters(self, n: int, dependencies: List[List[int]], k: int) -> int:
        G = [0] * n
        for x, y in dependencies:
            G[y-1] += 1 << (x-1) 
			  # node in dependencies are 1-indexed, everything below will be 0-indexed.
			  # G[x] = 0b10001 means the prerequisite of x is 0 and 4 (0th and 4th bit set.)
        P2 = [1<<y for y in range(n)]
        start = 0
        goal = 2**n-1
        d = collections.deque([(start,0)])
        seen = [0] * (2 ** n)

        while d:
            s, steps = d.popleft()
            available = [P2[y] for y in range(n) if (s & G[y] == G[y]) and (s & P2[y] == 0)]
			      # (s & G[y] == G[y]) means all prerequisite has been taken, 
			      # (s & P2[y] == 0) means y itself has not been taken.
            
            if len(available) <= k:
                # only ≤ k courses are available, take all of them.
                s += sum(available)
                if s == goal: 
                    return steps + 1
                if not seen[s]:
                    d.append((s,steps+1))
					          seen[s] = 1
            else:
			          # iterate through possible combinations
                for batch in itertools.combinations(available, k):
                    diff = sum(batch)
                    t = s + diff
                    if t == goal: return steps + 1
                    if not seen[t]:
                        d.append((t, steps+1))
                        seen[t] = 1

if __name__ == "__main__":
    sol = Solution()
    d = [[2,1],[3,1],[1,4]] 
    k = 2
    res = sol.minNumberOfSemesters(d, k)
    print("res is: ", res)