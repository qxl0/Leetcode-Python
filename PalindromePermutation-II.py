class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        count = Counter(s)
        if len([i for i in count.values() if count[i] % 2 == 1]) > 1:
            return []
        even = [i for i in count.keys() if count[i] % 2 == 0]
        odd = [i for i in count.keys() if count[i] % 2 == 1]

        perm = []

        def swap(s, i, j):
            tmp = s[i]
            s[i] = s[j]
            s[j] = tmp

        def generate(st, idx, cur):
            print(cur)
            if idx == len(st):
                perm.append(cur)
                return
            for i in range(idx + 1, len(st)):
                if st[idx] != st[i]:
                    # swap(st, idx, i)
                    generate(st, idx + 1, cur + [s[i]])
                    # swap(st, i, idx)

        generate(even, 0, [])

        print(perm)


if __name__ == "__main__":
    sol = Solution()
    s = "aabbcce"
    res = sol.generatePalindromes(s)
    print(res)
