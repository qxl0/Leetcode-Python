class Solution:
    def findSubstringInWraproundString(self, p):
        res = {i: 1 for i in p}
        l = 1
        for i, j in zip(p, p[1:]):
            print(i, j, l, res[j])
            l = l + 1 if (ord(j) - ord(i)) % 26 == 1 else 1
            res[j] = max(res[j], l)
        print(res)
        return sum(res.values())


if __name__ == "__main__":
    sol = Solution()
    res = sol.findSubstringInWraproundString("zaba")
    print(res)
