"""
423. Reconstruct Original Digits from English
Medium

606

2051

Add to List

Share
Given a string s containing an out-of-order English representation of digits 0-9, return the digits in ascending order.
"""


from collections import Counter
from math import floor
from typing import List


class Solution:
    def originalDigits(self, s: str) -> str:
        counter = Counter(s)
        Digits = [
            "zero",
            "two",
            "four",
            "six",
            "eight",
            "one",
            "three",
            "five",
            "seven",
            "nine",
        ]
        Corres = [0, 2, 4, 6, 8, 1, 3, 5, 7, 9]
        Cnts = [Counter(digit) for digit in Digits]
        Found = [0] * 10

        for it, C in enumerate(Cnts):
            k = min(counter[x] // C[x] for x in C)
            for i in C.keys():
                C[i] *= k
            counter -= C
            Found[Corres[it]] = k
        return "".join([str(i) * Found[i] for i in range(10)])


class Solution2:
    def originalDigits(self, s: str) -> str:
        n = [0] * 10
        counter = Counter(s)
        n[0] = counter["z"]
        n[2] = counter["w"]
        n[4] = counter["u"]
        n[6] = counter["x"]
        n[8] = counter["g"]
        n[1] = counter["o"] - n[0] - n[2] - n[4]
        n[3] = counter["r"] - n[0] - n[4]
        n[5] = counter["f"] - n[4]
        n[7] = counter["s"] - n[6]
        n[9] = counter["i"] - n[6] - n[8] - n[5]

        output = []
        for i in range(10):
            output.append(str(i) * n[i])

        return "".join(output)


if __name__ == "__main__":
    sol = Solution2()
    s = "fiviefuro"
    res = sol.originalDigits(s)
    print(res)
