from collections import defaultdict


class Solution:
    def group_anagrams(self, strs):
        d = {}
        for w in strs:
            key = tuple(sorted(w))
            d[key] = d.get(key, []) + [w]
        return d.values()


class Solution2:
    def group_anagrams(self, strs):
        d = defaultdict(list)
        for w in strs:
            key = tuple(sorted(w))
            d[key] += [w]
        return d.values()


class Solution3:
    def group_anagrams(self, strs):
        res = defaultdict(list)
        for w in strs:
            count = [0] * 26
            for c in w:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(w)
        return res.values()


if __name__ == "__main__":
    sol = Solution3()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    res = sol.group_anagrams(strs)
    print(res)
