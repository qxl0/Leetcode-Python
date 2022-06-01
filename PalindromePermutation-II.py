from collections import Counter
from typing import List


class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        count = Counter(s)
        res = []
        odd = [i for i in count.keys() if count[i] % 2 == 1]
        if len(odd) > 1:
            return res

        def generate(cur=""):
            if not count:
                res.append(cur)
                return

            for c in list(count.keys()):
                if count[c]:
                    count[c] -= 2
                    if count[c] == 0:
                        del count[c]
                    generate(c + cur + c)
                    count[c] += 2

        if len(odd) == 0:
            generate()
        if len(odd) == 1:
            oddchar = odd[0]
            count[oddchar] -= 1
            if count[oddchar] == 0:
                del count[oddchar]
            generate(oddchar)
        return res


if __name__ == "__main__":
    sol = Solution()
    s = "aabbcce"
    res = sol.generatePalindromes(s)
    print(res)
