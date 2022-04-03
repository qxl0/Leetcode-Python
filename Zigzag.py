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
        pass


if __name__ == "__main__":
    sol = Solution()
    s = "PAYPALISHIRING"
    numrows = 3
    res = sol.convert(s, numRows)
    print(res)
