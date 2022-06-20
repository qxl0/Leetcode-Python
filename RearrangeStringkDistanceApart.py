from collections import Counter, deque
from heapq import heapify, heappush, heappop


class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k < 2:
            return s
        q = deque([])  # to maintain used char, keep size k-1
        h = [(-count, ch) for ch, count in Counter(s).items()]
        heapify(h)

        ans = []
        while h:
            count, ch = heappop(h)
            ans.append(ch)
            if q and len(q) == k - 1:
                next_item = q.popleft()
                if next_item[0] < 0:
                    heappush(h, next_item)
            q.append((count + 1, ch))
        if len(ans) != len(s):
            return ""
        return "".join(ans)


if __name__ == "__main__":
    sol = Solution()
    s = "aabbcc"
    k = 3
    res = sol.rearrangeString(s, k)
    print("result is: ", res)
