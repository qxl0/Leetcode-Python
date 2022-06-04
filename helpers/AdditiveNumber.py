class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        ans = []
        isAdd = False

        def dfs(i):
            nonlocal isAdd
            if isAdd:
                return
            if i == n:
                if len(ans) > 2:
                    isAdd = True
                    return
            for j in range(i + 1, n + 1):
                if isAdd:
                    return
                cur = int(num[i:j])
                if len(num[i:j]) >= 2 and num[i] == "0":
                    continue
                if len(ans) < 2:
                    ans.append(cur)
                    dfs(j)
                    ans.pop()
                elif ans[-1] + ans[-2] == cur:
                    ans.append(cur)
                    dfs(j)
                    ans.pop()

        dfs(0)
        return isAdd


if __name__ == "__main__":
    sol = Solution()
    # s = "112358"
    s = "111"
    res = sol.isAdditiveNumber(s)
    print(res)
