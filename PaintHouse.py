from typing import List


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        memo = {}

        def helper(cur, color):
            if (cur, color) in memo:
                return memo[(cur, color)]
            total_cost = costs[cur][color]
            if cur == n - 1:
                pass
            elif color == 0:
                total_cost += min(helper(cur + 1, 1), helper(cur + 1, 2))
            elif color == 1:
                total_cost += min(helper(cur + 1, 0), helper(cur + 1, 1))
            else:
                total_cost += min(helper(cur + 1, 0), helper(cur + 1, 1))

            memo[(cur, color)] = total_cost
            return total_cost

        if not costs:
            return 0
        return min(helper(0, 0), helper(0, 1), helper(0, 2))


if __name__ == "__main__":
    sol = Solution()
    costs = [[17, 2, 17], [16, 16, 5], [14, 3, 19]]
    res = sol.minCost(costs)
    print("Ans is: ", res)
