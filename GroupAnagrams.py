class Solution:
    def group_anagrams(self, strs):
        d = {}
        for w in strs:
            key = tuple(sorted(w))
            d[key] = d.get(key, []) + [w]
        return d.values()


if __name__ == "__main__":
    sol = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    res = sol.group_anagrams(strs)
    print(res)
