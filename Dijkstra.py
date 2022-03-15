import collections
import heapq


class Solution:
    # def network_delayTime(self, times: List[List[int]], N: int, K: int) -> int:
    def networkDelayTime(self, times, N, K):
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        priority_queue = [(0, K)]
        shortest_path = {}
        while priority_queue:
            w, v = heapq.heappop(priority_queue)
            if v not in shortest_path:
                shortest_path[v] = w
                for v_i, w_i in graph[v]:
                    heapq.heappush(priority_queue, (w + w_i, v_i))

        if len(shortest_path) == N:
            return max(shortest_path.values())
        else:
            return -1

    def network_delaytime2(self, times, n, k):
        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u].append([v, w])
        minq = [(0, k)]
        visited = {}
        while minq:
            curr_w, curr_n = heapq.heappop(minq)
            if curr_n not in visited:
                visited[curr_n] = curr_w
                for new_n, new_w in edges[curr_n]:
                    heapq.heappush(minq, (curr_w + new_w, new_n))
        return max(visited.values()) if len(visited) == n else -1

    def networkDelayTime3(self, times, n, k):
        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u].append([v, w])
        minq = [(0, k)]
        visited = {}
        while minq:
            w, v = heapq.heappop(minq)  # weight, node
            if v not in visited:
                visited[v] = w
                for c_v, c_w in edges[v]:
                    heapq.heappush(minq, (c_w + w, c_v))
        return max(visited.values()) if len(visited) == n else -1


if __name__ == "__main__":
    sol = Solution()
    # times = [
    #     [1, 2, 1],
    #     [1, 4, 10],
    #     [2, 3, 3],
    #     [1, 3, 5],
    #     [4, 3, 1],
    #     [3, 5, 2],
    #     [4, 5, 2],
    # ]
    # n = 5
    # k = 1
    # times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    # n = 4
    # k = 2
    # times = [[1, 2, 1], [2, 3, 7], [1, 3, 4], [2, 1, 2]]
    # n = 3
    # k = 1
    times = [[1, 2, 1], [2, 3, 7], [1, 3, 4], [2, 1, 2]]
    n = 3
    k = 1
    res = sol.networkDelayTime3(times, n, k)
    print(res)
