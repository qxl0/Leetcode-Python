class Solution:
    def lastRemaining(self, n: int) -> int:
        ans = [i for i in range(1, n + 1)]
        left = True
        while len(ans) > 1:
            tmp = []
            if left:
                for i in range(1, len(ans), 2):
                    tmp.append(ans[i])
            else:
                for i in range(len(ans) - 1, -1, 2):
                    tmp.append(ans[i])
                tmp = tmp[::-1]
                print(tmp)
            ans = tmp[:]
            # print(ans)
            left = not left
        return ans[0]


if __name__ == "__main__":
    sol = Solution()
    n = 9
    res = sol.lastRemaining(n)
    print("Ans is: ", res)
