from collections import Counter
from typing import List


class Solution:
    def numberToWords(self, num: int) -> str:
        lessthan20 = [
            "",
            "One",
            "Two",
            "Three",
            "Four",
            "Five",
            "Six",
            "Seven",
            "Eight",
            "Nine",
            "Ten",
            "Eleven",
            "TWelve",
            "Thirteen",
            "Fourteen",
            "Fifteen",
            "Sixteen",
            "Seventeen",
            "Eighteen",
            "Nineteen",
        ]
        tens = [
            "",
            "Ten",
            "Twenty",
            "Thirty",
            "Fourty",
            "Fifty",
            "Sixty",
            "Seventy",
            "Eighty",
            "Ninety",
        ]
        thousands = ["", "Thousand", "Million", "Billion"]

        def helper(num):
            if num == 0:
                return ""
            elif num < 20:
                return lessthan20[num]
            elif num < 100:
                return tens[num // 10] + " " + helper(num % 10)
            else:
                return lessthan20[num // 100] + " Hundred " + helper(num % 100)

        if num == 0:
            return "Zero"
        res = " "
        for i in range(len(thousands)):
            if num % 1000 != 0:
                res = helper(num % 1000) + " " + thousands[i] + " " + res
                num //= 1000
        return res.rstrip()


if __name__ == "__main__":
    sol = Solution()
    n = 3
    res = sol.findCelebrity(n)
    print(res)
