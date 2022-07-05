from typing import List


class Solution:
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        n = len(scores)
        adj = {i: [] for i in range(n)}
        for a, b in edges:
            adj[a].append((scores[b], b))
            adj[b].append((scores[a], a))

        for i in range(n):
            adj[i].sort(key=lambda x: -x[0])
            if len(adj[i]) > 3:
                adj[i] = adj[i][:3]
        ret = -1
        for i, j in edges:
            for _, ii in adj[i]:
                for _, jj in adj[j]:
                    if ii != jj and ii != j and jj != i:
                        score = scores[ii] + scores[jj] + scores[i] + scores[j]
                        # print(f'{ii,i,j,jj}: {score}')
                        ret = max(ret, score)
                        break
        return ret


if __name__ == "__main__":
    sol = Solution()
    scores = [5, 2, 9, 8, 4]
    edges = [[0, 1], [1, 2], [2, 3], [0, 2], [1, 3], [2, 4]]
    res = sol.maximumScore(scores, edges)
    print("Ans is: ", res)
