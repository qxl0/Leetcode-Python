class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        import heapq
        from collections import defaultdict

        # Make graph
        adj_list = defaultdict(list)
        for u, v, w in flights:
            adj_list[u].append((v, w))

        prior_queue = [(0, -1, src)]  # weight, steps, node

        while prior_queue:
            cost, steps, node = heapq.heappop(prior_queue)

            if steps > k:
                continue

            if node == dst:
                return cost

            for neighb, weight in adj_list[node]:
                heapq.heappush(prior_queue, (cost + weight, steps + 1, neighb))

        return -1


if __name__ == "__main__":
    s = Solution()
    n = 3
    flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    src = 0
    dst = 2
    k = 1
    res = s.findCheapestPrice(n, flights, src, dst, k)
    print(res)
