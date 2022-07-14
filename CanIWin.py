class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        h = {}

        def dfs(state, sum):
            if state in h:
                return h[state]
            for i in range(1, maxChoosableInteger + 1):
                if (state >> i) & 1:
                    continue
                if sum + i >= desiredTotal:
                    h[state] = True
                    return True
                if dfs(state + (1 << i), sum + i) == False:
                    h[state] = True
                    return True
            h[state] = False
            return False

        return dfs(0, 0)


if __name__ == "__main__":
    sol = Solution()
    maxChoosableInteger = 5
    desiredTotal = 50
    res = sol.canIWin(maxChoosableInteger, desiredTotal)
    print(res)
