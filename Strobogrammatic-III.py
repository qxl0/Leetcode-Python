"""
**248. Strobogrammatic Number III**

**Hard**

271

172

Add to List

Share

Given two strings low and high that represent two integers `low` and `high` where `low <= high`, return *the number 
of **strobogrammatic numbers** in the range* `[low, high]`.

A **strobogrammatic number** is a number that looks the same when rotated `180` degrees (looked at upside down)
"""


class Solution:
    def strobogrammaticInRange(self, low, high):
        a = self.below(int(high))
        b = self.below(int(low), include=False)
        return a - b if a > b else 0

    """
    get how many strobogrammatic numbers less than n
    """

    def below(self, n, include=True):
        res = 0
        for i in range(1, len(str(n))):
            res += self.number(i)
        l = self.strobogrammatic(len(str(n)))
        """
        filter num larger than n and start with 0
        """
        if include:
            l = [num for num in l if (len(num) == 1 or num[0] != "0") and int(num) <= n]
        else:
            l = [num for num in l if (len(num) == 1 or num[0] != "0") and int(num) < n]
        return res + len(l)

    """
    get strobogrammatic numbers with length l
    number start with 0 would be included
    """

    def strobogrammatic(self, l):
        res = []
        if l == 1:
            return ["0", "1", "8"]
        if l == 2:
            return ["00", "11", "69", "96", "88"]
        for s in self.strobogrammatic(l - 2):
            res.append("0" + s + "0")
            res.append("1" + s + "1")
            res.append("6" + s + "9")
            res.append("8" + s + "8")
            res.append("9" + s + "6")
        return res

    """
    get number of strobogrammatic numbers of length l
    """

    def number(self, l):
        if l == 0:
            return 0
        """
        If l is an even number, the first digit has four choices (1,6,8,9). digits 
        at other position have five choices(0,1,6,8,9)
        """
        if l % 2 == 0:
            return 4 * (5 ** (l / 2 - 1))
        # If l is an odd number, the first digit has four choices (1,6,8,9) and digit
        # at the middle has 3 choices (0,1,8),other digits have 5 choices.
        # digit at other position could be 0,1,6,8,9
        elif l == 1:
            return 3
        else:
            return 3 * (5 ** (l / 2 - 1)) * 4


class Solution2:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        def stro(n):
            res = []
            if n == 1:
                return ["0", "1", "8"]
            elif n == 2:
                return ["00", "11", "69", "88", "96"]
            else:
                for s in stro(n - 2):
                    res.append("0" + s + "0")
                    res.append("1" + s + "1")
                    res.append("6" + s + "9")
                    res.append("8" + s + "8")
                    res.append("9" + s + "6")
            return res

        def getStroNumber(low, include=True):
            res = []
            for i in range(1, len(str(low)) + 1):
                res.extend(stro(i))
            if include:
                return [
                    s for s in res if (len(s) == 1 or s[0] != "0") and int(s) <= low
                ]
            else:
                return [s for s in res if (len(s) == 1 or s[0] != "0") and int(s) < low]

        totalhigh = len(getStroNumber(int(high), True))
        totallow = len(getStroNumber(int(low), False))
        return totalhigh - totallow


if __name__ == "__main__":
    sol = Solution2()
    low = "50"
    high = "100"
    res = sol.strobogrammaticInRange(low, high)
    print("result is: ", res)
