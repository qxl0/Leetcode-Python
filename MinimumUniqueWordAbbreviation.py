class Solution:
    def minAbbreviation(self, target, dictionary):
        m = len(target)
        diffs = {
            sum(2**i for i, c in enumerate(word) if target[i] != c)
            for word in dictionary
            if len(word) == m
        }
        if not diffs:
            return str(m)
        bits = max(
            (i for i in range(2**m) if all(d & i for d in diffs)),
            key=lambda bits: sum((bits >> i) & 3 == 0 for i in range(m - 1)),
        )
        s = "".join(target[i] if bits & 2**i else "#" for i in range(m))
        return re.sub("#+", lambda m: str(len(m.group())), s)


if __name__ == "__main__":
    sol = Solution()
    target = "apple"
    dictionary = ["blade", "angry"]
    res = sol.minAbbreviation(target, dictionary)
    print("Ans is: ", res)
