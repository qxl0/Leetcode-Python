from typing import List


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        import heapq
        from collections import defaultdict

        # Make graph
        adj_list = defaultdict(list)  # list, dict,
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

    def findCheapestPrice2(
        self, n: int, flights: List[List[int]], src: int, dst: int, K: int
    ) -> int:
        price_table = [float("inf") for _ in range(n)]
        price_table[src] = 0
        for source, dest, price in flights:
            if source == src:
                price_table[dest] = price
        for transfer in range(0, K):
            current_price = [*price_table]
            for source, dest, price in flights:
                # when we get a s --(p)-> d, we can update current_price[d]
                current_price[dest] = min(
                    current_price[dest], price_table[source] + price
                )
            price_table = current_price
        if price_table[dst] == float("inf"):
            return -1
        else:
            return price_table[dst]


if __name__ == "__main__":
    s = Solution()
    n = 3
    flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    src = 0
    dst = 2
    k = 1
    # n = 5
    # flights = [[4, 1, 1], [1, 2, 3], [0, 3, 2], [0, 4, 10], [3, 1, 1], [1, 4, 3]]
    # src = 2
    # dst = 1
    # k = 1
    res = s.findCheapestPrice2(n, flights, src, dst, k)
    print(res)
