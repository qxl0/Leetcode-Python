class Solution:
    # def minAbbreviation(self, target, dictionary):
    #     m = len(target)
    #     diffs = {
    #         sum(2**i for i, c in enumerate(word) if target[i] != c)
    #         for word in dictionary
    #         if len(word) == m
    #     }
    #     if not diffs:
    #         return str(m)
    #     bits = max(
    #         (i for i in range(2**m) if all(d & i for d in diffs)),
    #         key=lambda bits: sum((bits >> i) & 3 == 0 for i in range(m - 1)),
    #     )
    #     s = "".join(target[i] if bits & 2**i else "#" for i in range(m))
    #     return re.sub("#+", lambda m: str(len(m.group())), s)
    def minAbbreviation(self, target, dictionary):
        def abbr(target, num):
            word, count = "", 0
            for w in target:
                if num & 1 == 1:
                    if count:
                        word += str(count)
                        count = 0
                    word += w
                else:
                    count += 1

                num >>= 1
            if count:
                word += str(count)
            return word

        m = len(target)

        # Figure out the different bits for a same length word in the dictionary
        diffs = []
        for word in dictionary:
            if len(word) != m:
                continue

            # The encoding is opposite
            bits = 0
            for i, char in enumerate(word):
                if char != target[i]:
                    bits += 2**i
            diffs += (bits,)

        # No word in dictionary has same length, return the shortest
        if not diffs:
            return str(m)

        abbrs = []
        for i in range(2**m):
            # This abbreviation at least has one word different to every words in the dictionary
            if all(d & i for d in diffs):
                abbrs += (abbr(target, i),)

        return min(abbrs, key=lambda x: len(x))

    def abbr(self, target, num):
        word, count = "", 0
        for w in target:
            if num & 1 == 1:
                if count:
                    word += str(count)
                    count = 0
                word += w
            else:
                count += 1

            num >>= 1
        if count:
            word += str(count)
        return word


if __name__ == "__main__":
    sol = Solution()
    # res = sol.abbr("apple", 0b1111)
    target = "apple"
    dictionary = ["blade"]
    res = sol.minAbbreviation(target, dictionary)
    print("Ans is: ", res)
