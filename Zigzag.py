"""
6. Zigzag Conversion
Medium

3521

8148

Add to List

Share
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
"""


from math import factorial
from typing import List


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        res = ""
        for r in range(numRows):
            dr = (numRows - 1) * 2  # gap for top and bottom rows
            for i in range(r, len(s), dr):  # dr is the gap
                res += s[i]
                if r > 0 and r < numRows - 1 and i + dr - 2 * r < len(s):
                    res += s[
                        i + dr - 2 * r
                    ]  # if mid rows, gap dr-2*r: r=1, dr-2;r=2:dr-4
        return res


if __name__ == "__main__":
    sol = Solution()
    s = "PAYPALISHIRING"
    numrows = 3
    res = sol.convert(s, numrows)
    print(res)
