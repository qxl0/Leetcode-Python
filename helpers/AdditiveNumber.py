class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        ans = []

        def dfs(i):
            print(ans)
            if i == n:
                return
            for j in range(i + 1, n):
                cur = int(num[i:j])
                if len(num[i:j]) >= 2 and num[i] == "0":
                    continue
                if len(ans) >= 2 and ans[-1] + ans[-2] == cur:
                    ans.append(cur)
                    dfs(j + 1)

        dfs(0)
        return len(ans) == n


if __name__ == "__main__":
    sol = Solution()
    s = "112358"
    res = sol.isAdditiveNumber(s)
    print(res)
