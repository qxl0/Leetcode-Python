class Solution:
    def encode(self, strs):
        res = ""
        for w in strs:
            res += w + ":;"
        return res

    def decode(self, strs):
        res = strs.split(":;")
        res = res[:-1]
        return res


if __name__ == "__main__":
    sol = Solution()
    strs = ["lint", "code", "love", "you"]
    res = sol.encode(strs)
    print(res)
    res2 = sol.decode(res)
    print(res2)
